from tap_kit.streams import Stream


class OffersStream(Stream):
    stream = 'offers'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='created_at',
        valid_replication_keys=['created_at'],
        incremental_search_key='updated_after',
        replication_method='incremental',
        selected_by_default=False
    ) 
    schema = \
        {
            "type": [
                "null",
                "object"
            ],
            "properties": {
                "id": {
                    "type": [
                        "null",
                        "integer"
                    ]
                },
                "version": {
                    "type": [
                        "null",
                        "integer"
                    ]
                },
                "application_id": {
                    "type": [
                        "null",
                        "integer"
                    ]
                },
                "job_id": {
                    "type": [
                        "null",
                        "integer"
                    ]
                },
                "created_at": {
                    "type": [
                        "null",
                        "string"
                    ],
                    "format": "date-time",
                },
                "resolved_at": {
                    "type": [
                        "null",
                        "string"
                    ],
                    "format": "date-time",
                },
                "sent_at": {
                    "type": [
                        "null",
                        "string"
                    ],
                    "format": "date-time",
                },
                "starts_at": {
                    "type": [
                        "null",
                        "string"
                    ],
                    "format": "date-time",
                },
                "status": {
                    "type": [
                        "null",
                        "string"
                    ]
                }

            }
        }
