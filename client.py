class NegativeHypothesisFailedPatchIndexerClient:
    def record_and_check_collision(self, candidate_patch_intent='MODIFY_THREAD_LOCK_INLINE', failure_reason='DEADLOCK_IN_ASYNC_LOOP'):
        return {
            'index_entry_id': 'neg_idx_8812',
            'disproved_hypothesis': candidate_patch_intent,
            'collision_detected': True,
            'blacklisted_approaches_count': 14,
            'recommended_divergence_strategy': 'USE_EVENT_LOOP_MUTEX_QUEUE',
            'loop_prevention_activated': True,
            'failure_index_url': 'https://astra.negative.genpark.ai/patches/8812.json'
        }
