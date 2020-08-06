import time
import boto3
import cazoo_logger


def create_cloudwatch_event(
    detail_type: str,
    detail: str,
    source: str,
    resources: list = [],
    additional_args: dict = {},
) -> dict:
    """Create a simple cloudwatch event"""
    return {
        "Source": source,
        "DetailType": detail_type,
        "Resources": resources,
        "Detail": detail,
        **additional_args,
    }


def put_events(
    Entries,
    log=cazoo_logger.empty(),
    client=boto3.client("events", region_name="eu-west-1"),
):
    """ Function to push events to CW Events
        and control possible errors
    """

    response = client.put_events(Entries=Entries)

    failed_entry_count: int = response.get("FailedEntryCount")
    if failed_entry_count != 0:
        event_logs = response.get("Entries")
        log.error(
            f"Could not push cloudwatch events. {failed_entry_count} events failed to push.",
            extra=event_logs,
        )
        raise Exception("Did not push all required events to cloudwatch")

    return response


class InvalidParameterException(Exception):
    pass


def push_events_in_chunks(
    events: list,
    chunk_size: int = 10,
    sleep_time: float = 0.2,
    raise_or_pass_exceptions: str = "raise",
    cw_client: boto3.client = boto3.client("events", region_name="eu-west-1"),
    logger=cazoo_logger.empty(),
) -> None:
    """
    Function to take in a list of events of length len(events)
    and fire off the events in chunks of size chunk_size
    with intervals of sleep_time
    """
    events_split = [
        events[i : i + chunk_size] for i in range(0, len(events), chunk_size)
    ]
    for chunk in events_split:
        try:
            put_events(chunk, log=logger, client=cw_client)
            time.sleep(sleep_time)  # reduce pressure on realtimedb
        except Exception as e:
            logger.error(
                "Failed to push chunk of events",
                extra={"chunk": chunk, "error message": str(e)},
            )
            if raise_or_pass_exceptions == "raise":
                raise
            elif raise_or_pass_exceptions == "pass":
                pass
            else:
                raise InvalidParameterException(
                    f"raise_or_pass_exceptions must be 'raise' or 'pass', not {raise_or_pass_exceptions}"
                )
