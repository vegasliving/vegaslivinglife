proxy
./cloud_sql_proxy -instances=vegas-living:us-central1:vegasliving=tcp:3306 \
                  -credential_file=vegasliving.json &