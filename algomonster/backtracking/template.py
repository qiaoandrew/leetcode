def backtracking_dfs_template(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    
    for edge in get_edges(start_idx):
        path.append(edge)
        dfs(start_idx + 1, path)
        path.pop()


def backtracking_dfs_with_pruning_template(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    
    for edge in get_edges(start_idx):
        # prune if needed
        if not is_valid(edge):
            continue
        path.append(edge)
        # increment start_idx
        dfs(start_idx + len(edge), path)
        path.pop()


def backtracking_dfs_with_pruning_and_additional_states_template(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    
    for edge in get_edges(start_idx, [...additional_states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional_states:
            update(...additional_states)
        dfs(start_idx + len(edge), path, [...additional_states])
        # revert (...additional_states) if necessary
        path.pop()

def dfs_with_aggregation_template(start_idx, [..additional_states]):
    if is_leaf(start_idx):
        return 1
    ans = initial_value
    for edge in get_edges(start_idx, [...additional_states]):
        if additional_states:
            update([...additional_states])
        ans = aggregage(ans, dfs(start_idx + len(edge), [...additional_states]))
        if additional_states:
            revert([...additional_states])
    return ans