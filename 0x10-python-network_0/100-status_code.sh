#!/bin/bash
# displays only the status code of the response.
curl -w "%{http_code}\n" "$1"
