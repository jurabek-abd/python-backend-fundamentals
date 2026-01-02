def format_push_event(event):
    return f"- Pushed to {event['payload']['ref'].split('/')[-1]} in {event['repo']['name']}"


def format_issue_comment_event(event):
    return f"- Commented on issue #{event['payload']['issue']['number']} in {event['repo']['name']}"


def format_pull_request_event(event):
    return f"- Opened pull request #{event['payload']['number']} in {event['repo']['name']}"


def format_activity(events):
    print("\nOutput:\n")

    for event in events:
        if event["type"] == "PushEvent":
            print(format_push_event(event))
        elif event["type"] == "IssueCommentEvent":
            print(format_issue_comment_event(event))
        elif event["type"] == "PullRequestEvent":
            print(format_pull_request_event(event))

    print("\n")
