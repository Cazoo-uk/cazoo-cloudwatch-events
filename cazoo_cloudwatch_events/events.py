import boto3
from typing import List
import boto3

def put_events(events, log, client=boto3.client("events", region_name='eu-west-1')):
    ''' Function to push events to CW Events
        and control possible errors
    '''

    cloudwatch_client = boto3.client('events', 'eu-west-1')
    response = cloudwatch_client.put_events(
        Entries=events
    )
    failed_entry_count: int = response.get("FailedEntryCount")
    if failed_entry_count != 0:
        event_logs: List[dict] = response.get("Entries")
        log.error(
            f"Could not push cloudwatch events. {failed_entry_count} events failed to push.",
            extra=event_logs)
        raise Exception("Did not push all required events to cloudwatch")
