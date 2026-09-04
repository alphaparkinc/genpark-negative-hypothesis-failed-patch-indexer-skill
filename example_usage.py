from client import NegativeHypothesisFailedPatchIndexerClient

def main():
    client = NegativeHypothesisFailedPatchIndexerClient()
    res = client.record_and_check_collision('SYNC_LOCK', 'DEADLOCK')
    print('Failed Patch Indexer: ' + res['index_entry_id'])
    print('Collision Detected: ' + str(res['collision_detected']) + ' | Strategy: ' + res['recommended_divergence_strategy'])
    print('Index URL: ' + res['failure_index_url'])

if __name__ == '__main__':
    main()
