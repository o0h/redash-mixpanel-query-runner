# redash-mixpanel-query-runner

redash query-runner for Mixpanel's JQL api.  
https://mixpanel.com/help/reference/jql

## Installation

1. Donwload `mixpanel_jql.py`
2. Copy `mixpanel_jql.py` to `/path/to/redash/redash/query_runner` on your redash server.
3. Modify environment var `REDASH_ADDITIONAL_QUERY_RUNNERS` to add `redash.query_runner.mixpanel_jql`

### Required
Mixpanel python client library is required.  
Download from [official page](https://mixpanel.com/help/reference/data-export-api) and set on your server.

## Usage
### Configure your API Secret
Add Mixpanel Jql as new datasource, then configure `Api secret` of yours.  
See: https://mixpanel.com/help/reference/data-export-api#authentication

### Run query
As Query, write jql.  
Like bellow:  
![Query Result Example](https://user-images.githubusercontent.com/907122/42751439-bfc111ac-8925-11e8-9b41-6b4fdc0f997b.png)

