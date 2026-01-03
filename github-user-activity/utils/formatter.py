def format_push_event(event):
    ref = event["payload"].get("ref", "")
    branch = ref.split("/")[-1] if ref else "unknown"
    return f"- Pushed to {branch} in {event['repo']['name']}"


def format_issue_comment_event(event):
    issue = event["payload"]["issue"]
    return (
        f"- Commented on issue #{issue['number']} "
        f"({issue['title']}) in {event['repo']['name']}"
    )


def format_pull_request_event(event):
    action = event["payload"]["action"]
    pr_number = event["payload"]["number"]
    repo = event["repo"]["name"]

    if action == "opened":
        return f"- Opened pull request #{pr_number} in {repo}"
    elif action == "closed":
        pr = event["payload"]["pull_request"]
        if pr.get("merged"):
            return f"- Merged pull request #{pr_number} in {repo}"
        return f"- Closed pull request #{pr_number} in {repo}"

    return f"- Updated pull request #{pr_number} in {repo}"


def format_create_event(event):
    ref_type = event["payload"]["ref_type"]
    ref = event["payload"].get("ref")

    if ref_type == "branch":
        return f"- Created branch {ref} in {event['repo']['name']}"
    elif ref_type == "tag":
        return f"- Created tag {ref} in {event['repo']['name']}"
    elif ref_type == "repository":
        return f"- Created repository {event['repo']['name']}"

    return f"- Created {ref_type} in {event['repo']['name']}"


def format_delete_event(event):
    ref_type = event["payload"]["ref_type"]
    ref = event["payload"]["ref"]
    return f"- Deleted {ref_type} {ref} in {event['repo']['name']}"


def format_issues_event(event):
    action = event["payload"]["action"]
    issue = event["payload"]["issue"]

    return (
        f"- {action.capitalize()} issue #{issue['number']} "
        f"({issue['title']}) in {event['repo']['name']}"
    )


def format_watch_event(event):
    return f"- Starred {event['repo']['name']}"


def format_fork_event(event):
    forkee = event["payload"]["forkee"]["full_name"]
    return f"- Forked {event['repo']['name']} to {forkee}"


FORMATTERS = {
    "PushEvent": format_push_event,
    "IssueCommentEvent": format_issue_comment_event,
    "PullRequestEvent": format_pull_request_event,
    "CreateEvent": format_create_event,
    "DeleteEvent": format_delete_event,
    "IssuesEvent": format_issues_event,
    "WatchEvent": format_watch_event,
    "ForkEvent": format_fork_event,
}


def format_activity(events):
    print("\nOutput:\n")

    for event in events:
        formatter = FORMATTERS.get(event["type"])
        if formatter:
            print(formatter(event))
        else:
            print(f"- {event['type']} in {event['repo']['name']}")

    print()
