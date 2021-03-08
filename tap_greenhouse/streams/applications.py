from tap_kit.streams import Stream


class ApplicationsStream(Stream):

    stream = 'applications'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='last_activity_at',
        valid_replication_keys=['last_activity_at'],
        incremental_search_key='last_activity_after',
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "candidate_id": {
            "type": ["null", "integer"]
        },
        "prospect": {
            "type": ["null", "string", "boolean"]
        },
        "applied_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
        },
        "rejected_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
        "last_activity_at": {
            "type": [
                "null",
                "string"
            ],
            "format": "date-time",
        },
        "location": {
            "type": ["null", "string"]
        },
        "source": {
            "type": ["null", "object"],
            "properties": {
                "public_name": {"type": ["null", "string"]},
                "id": {"type": ["null", "number"]},
            }
        },
        "credited_to": {
            "type": ["null", "object"],
            "properties": {
                "name": {
                    "type": ["null", "string"]
                },
                "id": {
                    "type": ["null", "number"]
                },
                "employee_id": {
                    "type": ["null", "number"]
                },
            }
        },
        "rejection_reason": {
            "type": ["null", "object"],
            "properties": {
                "name": {
                    "type": ["null", "string"],
                },
                "id": {
                    "type": ["null", "number"],
                },
            }
        },
        "rejection_details": {
            "type": ["null", "object"],
        },
        "prospective_office": {
            "type": ["null", "object"],
        },
        "prospective_department": {
            "type": ["null", "object"],
        },
        "jobs": {
            "type": ["null", "array"]
        },
        "status": {
            "type": ["null", "string"]
        },
        "current_stage": {
            "type": ["null", "object"],
            "properties": {
                "name": {
                    "type": ["null", "string"]
                },
                "id": {
                    "type": ["null", "number"]
                },
            }
        },
        "attachments": {
            "type": ["null", "array"],
        },
        "answers": {
            "type": ["null", "array"]
        },
        "prospect_detail": {
            "type": ["null", "object"],
            "properties": {
                "prospect_stage": {"type": ["null", "object"]},
                "prospect_pool": {"type": ["null", "object"]},
                "prospect_owner": {"type": ["null", "object"]}
            }
        },
        "custom_fields": {
            "properties": {}
        },
        "keyed_custom_fields": {
            "properties": {}
        }
    }
}
