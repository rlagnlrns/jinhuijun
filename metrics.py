external_metrics_list = [
    'Sets_Ops/sec', 'Sets_Hits/sec', 'Sets_Misses/sec', 'Sets_Latency', 'Sets_KB/sec',
    'Gets_Ops/sec', 'Gets_Hits/sec', 'Gets_Misses/sec', 'Gets_Latency', 'Gets_KB/sec',
    'Waits_Ops/sec', 'Waits_Hits/sec', 'Waits_Misses/sec', 'Waits_Latency', 'Waits_KB/sec',
    'Totals_Ops/sec', 'Totals_Hits/sec', 'Totals_Misses/sec', 'Totals_Latency', 'Totals_KB/sec'    
]


internal_metrics_list = [
'redis_version', 'redis_git_sha1', 'redis_git_dirty', 'redis_build_id', 'redis_mode', 'os', 'arch_bits', 'multiplexing_api', 'atomicvar_api', 'gcc_version', 'process_id', 'process_supervised', 'run_id', 'tcp_port', 'server_time_usec', 'uptime_in_seconds', 'uptime_in_days', 'hz', 'configured_hz', 'lru_clock', 'executable', 'config_file', 'io_threads_active',
'connected_clients', 'cluster_connections', 'maxclients', 'client_recent_max_input_buffer', 'client_recent_max_output_buffer', 'blocked_clients', 'tracking_clients', 'clients_in_timeout_table',
'used_memory', 'used_memory_human', 'used_memory_rss', 'used_memory_rss_human', 'used_memory_peak', 'used_memory_peak_human', 'used_memory_peak_perc', 'used_memory_overhead', 'used_memory_startup', 'used_memory_dataset', 'used_memory_dataset_perc', 'allocator_allocated', 'allocator_active', 'allocator_resident', 'total_system_memory', 'total_system_memory_human', 'used_memory_lua', 'used_memory_lua_human', 'used_memory_scripts', 'used_memory_scripts_human', 'number_of_cached_scripts', 'maxmemory', 'maxmemory_human', 'maxmemory_policy', 'allocator_frag_ratio', 'allocator_frag_bytes', 'allocator_rss_ratio', 'allocator_rss_bytes', 'rss_overhead_ratio', 'rss_overhead_bytes', 'mem_fragmentation_ratio', 'mem_fragmentation_bytes', 'mem_not_counted_for_evict', 'mem_replication_backlog', 'mem_clients_slaves', 'mem_clients_normal', 'mem_aof_buffer', 'mem_allocator', 'active_defrag_running', 'lazyfree_pending_objects', 'lazyfreed_objects',
'loading', 'current_cow_size', 'current_fork_perc', 'current_save_keys_processed', 'current_save_keys_total', 'rdb_changes_since_last_save', 'rdb_bgsave_in_progress', 'rdb_last_save_time', 'rdb_last_bgsave_status', 'rdb_last_bgsave_time_sec', 'rdb_current_bgsave_time_sec', 'rdb_last_cow_size', 'aof_enabled', 'aof_rewrite_in_progress', 'aof_rewrite_scheduled', 'aof_last_rewrite_time_sec', 'aof_current_rewrite_time_sec', 'aof_last_bgrewrite_status', 'aof_last_write_status', 'aof_last_cow_size', 'module_fork_in_progress', 'module_fork_last_cow_size', 'aof_current_size', 'aof_base_size', 'aof_pending_rewrite', 'aof_buffer_length', 'aof_rewrite_buffer_length', 'aof_pending_bio_fsync', 'aof_delayed_fsync',
'total_connections_received', 'total_commands_processed', 'instantaneous_ops_per_sec', 'total_net_input_bytes', 'total_net_output_bytes', 'instantaneous_input_kbps', 'instantaneous_output_kbps', 'rejected_connections', 'sync_full', 'sync_partial_ok', 'sync_partial_err', 'expired_keys', 'expired_stale_perc', 'expired_time_cap_reached_count', 'expire_cycle_cpu_milliseconds', 'evicted_keys', 'keyspace_hits', 'keyspace_misses', 'pubsub_channels', 'pubsub_patterns', 'latest_fork_usec', 'total_forks', 'migrate_cached_sockets', 'slave_expires_tracked_keys', 'active_defrag_hits', 'active_defrag_misses', 'active_defrag_key_hits', 'active_defrag_key_misses', 'tracking_total_keys', 'tracking_total_items', 'tracking_total_prefixes', 'unexpected_error_replies', 'total_error_replies', 'dump_payload_sanitizations', 'total_reads_processed', 'total_writes_processed', 'io_threaded_reads_processed', 'io_threaded_writes_processed',
'role', 'connected_slaves', 'master_failover_state', 'master_replid', 'master_replid2', 'master_repl_offset', 'second_repl_offset', 'repl_backlog_active', 'repl_backlog_size', 'repl_backlog_first_byte_offset', 'repl_backlog_histlen',
'used_cpu_sys', 'used_cpu_user', 'used_cpu_sys_children', 'used_cpu_user_children', 'used_cpu_sys_main_thread', 'used_cpu_user_main_thread',
'cluster_enabled',
'db0:keys', 'expires', 'avg_ttl'
]