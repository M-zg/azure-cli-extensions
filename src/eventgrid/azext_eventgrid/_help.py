# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.help_files import helps  # pylint: disable=unused-import


helps['eventgrid'] = """
    type: group
    short-summary: Manage Azure Event Grid topics, event subscriptions, domains and domain topics.
    """
helps['eventgrid topic'] = """
    type: group
    short-summary: Manage topics.
    """
helps['eventgrid topic create'] = """
    type: command
    short-summary: Create a topic.
    examples:
        - name: Create a new topic.
          text: az eventgrid topic create -g rg1 --name topic1 -l westus2
        - name: Create a new topic with custom input mappings.
          text: az eventgrid topic create -g rg1 --name topic1 -l westus2 --input-schema customeventschema --input-mapping-fields topic=myTopicField eventType=myEventTypeField --input-mapping-default-values subject=DefaultSubject dataVersion=1.0
        - name: Create a new topic that accepts events published in CloudEvents V0.1 schema.
          text: az eventgrid topic create -g rg1 --name topic1 -l westus2 --input-schema cloudeventv01schema
    """
helps['eventgrid topic update'] = """
    type: command
    short-summary: Update a topic.
    examples:
        - name: Update the properties of an existing topic.
          text: az eventgrid topic update -g rg1 --name topic1 --tags Dept=IT
    """
helps['eventgrid topic delete'] = """
    type: command
    short-summary: Delete a topic.
    examples:
        - name: Delete a topic.
          text: az eventgrid topic delete -g rg1 --name topic1
    """
helps['eventgrid topic list'] = """
    type: command
    short-summary: List available topics.
    examples:
        - name: List all topics in the current Azure subscription.
          text: az eventgrid topic list
        - name: List all topics in a resource group.
          text: az eventgrid topic list -g rg1
    """
helps['eventgrid topic show'] = """
    type: command
    short-summary: Get the details of a topic.
    examples:
        - name: Show the details of a topic.
          text: az eventgrid topic show -g rg1 -n topic1
        - name: Show the details of a topic based on resource ID.
          text: az eventgrid topic show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
    """
helps['eventgrid topic key'] = """
    type: group
    short-summary: Manage shared access keys of a topic.
    """
helps['eventgrid topic key list'] = """
    type: command
    short-summary: List shared access keys of a topic.
    """
helps['eventgrid topic key regenerate'] = """
    type: command
    short-summary: Regenerate a shared access key of a topic.
    """
helps['eventgrid domain'] = """
    type: group
    short-summary: Manage event domains.
    """
helps['eventgrid domain create'] = """
    type: command
    short-summary: Create a domain.
    examples:
        - name: Create a new domain.
          text: az eventgrid domain create -g rg1 --name domain1 -l westus2
        - name: Create a new domain with custom input mappings.
          text: az eventgrid domain create -g rg1 --name domain1 -l westus2 --input-schema customeventschema --input-mapping-fields topic=mytopicField eventType=myEventTypeField --input-mapping-default-values subject=DefaultSubject dataVersion=1.0
        - name: Create a new domain that accepts events published in CloudEvents V0.1 schema.
          text: az eventgrid domain create -g rg1 --name domain1 -l westus2 --input-schema cloudeventv01schema
    """
helps['eventgrid domain update'] = """
    type: command
    short-summary: Update a domain.
    examples:
        - name: Update the properties of an existing domain.
          text: az eventgrid domain update -g rg1 --name domain1 --tags Dept=IT
    """
helps['eventgrid domain delete'] = """
    type: command
    short-summary: Delete a domain.
    examples:
        - name: Delete a domain.
          text: az eventgrid domain delete -g rg1 --name domain1
    """
helps['eventgrid domain list'] = """
    type: command
    short-summary: List available domains.
    examples:
        - name: List all domains in the current Azure subscription.
          text: az eventgrid domain list
        - name: List all domains in a resource group.
          text: az eventgrid domain list -g rg1
    """
helps['eventgrid domain show'] = """
    type: command
    short-summary: Get the details of a domain.
    examples:
        - name: Show the details of a domain.
          text: az eventgrid domain show -g rg1 -n domain1
        - name: Show the details of a domain based on resource ID.
          text: az eventgrid domain show --ids /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
    """
helps['eventgrid domain key'] = """
    type: group
    short-summary: Manage shared access keys of a domain.
    """
helps['eventgrid domain topic'] = """
    type: group
    short-summary: Manage event domain topics.
    """
helps['eventgrid domain topic create'] = """
    type: command
    short-summary: Create a domain topic under a domain.
    examples:
        - name: Create a new domain topic under domain.
          text: az eventgrid domain topic create -g rg1 --domain-name domain1 --name domaintopic1
    """
helps['eventgrid domain topic delete'] = """
    type: command
    short-summary: Delete a domain topic under a domain.
    examples:
        - name: Delete a domain topic.
          text: az eventgrid domain topic delete -g rg1 --domain-name domain1 --name domaintopic1
    """
helps['eventgrid domain key list'] = """
    type: command
    short-summary: List shared access keys of a domain.
    """
helps['eventgrid domain key regenerate'] = """
    type: command
    short-summary: Regenerate a shared access key of a domain.
    """
helps['eventgrid domain topic list'] = """
    type: command
    short-summary: List available topics in a domain.
    examples:
        - name: List all topics in a domain.
          text: az eventgrid domain topic list -g rg1 --domain-name domain1
    """
helps['eventgrid domain topic show'] = """
    type: command
    short-summary: Get the details of a domain topic.
    examples:
        - name: Show the details of a domain topic.
          text: az eventgrid domain topic show -g rg1 --domain-name domain1 --name topic1
    """
helps['eventgrid event-subscription'] = """
    type: group
    short-summary: Manage event subscriptions.
    long-summary: Manage event subscriptions for an Event Grid topic, domain, domain topic, Azure subscription, resource group or for any other Azure resource that supports event notifications.
    """
helps['eventgrid event-subscription create'] = """
    type: command
    short-summary: Create a new event subscription.
    parameters:
        - name: --advanced-filter
          short-summary: An advanced filter enables filtering of events based on a specific event property.
          long-summary: |
            Usage:                     --advanced-filter KEY[.INNERKEY] FILTEROPERATOR VALUE [VALUE ...]
            StringIn:                  --advanced-filter data.Color StringIn Blue Red Orange Yellow
            StringNotIn:               --advanced-filter data.Color StringNotIn Blue Red Orange Yellow
            StringContains:            --advanced-filter subject StringContains Blue Red
            StringBeginsWith:          --advanced-filter subject StringBeginsWith Blue Red
            StringEndsWith:            --advanced-filter subject StringEndsWith img png jpg
            NumberIn:                  --advanced-filter data.property1 NumberIn 5 10 20
            NumberNotIn:               --advanced-filter data.property2 NumberNotIn 100 200 300
            NumberLessThan:            --advanced-filter data.property3 NumberLessThan 100
            NumberLessThanOrEquals:    --advanced-filter data.property2 NumberLessThanOrEquals 100
            NumberGreaterThan:         --advanced-filter data.property3 NumberGreaterThan 100
            NumberGreaterThanOrEquals: --advanced-filter data.property2 NumberGreaterThanOrEquals 100
            BoolEquals:                --advanced-filter data.property3 BoolEquals true
            Multiple advanced filters can be specified by using more than one `--advanced-filter` argument.
        - name: --source-resource-id
          short-summary: Fully qualified identifier of the Azure resource to which the event subscription needs to be created.
          long-summary: |
            Usage:                      --source-resource-id Azure-Resource-ID
            For Azure subscription:     --source-resource-id /subscriptions/{SubID}
            For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
            For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
            For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
            For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
            For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
        - name: --deadletter-endpoint
          short-summary: The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
          long-summary: |
            Example: --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/containerName
        - name: --endpoint-type
          short-summary: The type of the destination endpoint. It is expected that the destination endpoint be created and available for use before executing any Event Grid command.

    examples:
        - name: Create a new event subscription for an Event Grid topic, using default filters.
          text: |
            az eventgrid event-subscription create --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Create a new event subscription for an Azure subscription subscription, using default filters.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id /subscriptions/{SubID} \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Create a new event subscription for a resource group, using default filters.
          text: |
            az eventgrid event-subscription create --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Create a new event subscription for a storage account, using default filters.
          text: |
            az eventgrid event-subscription create --name es3 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1"  \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Create a new event subscription for a storage account, using advanced filters.
          text: |
            az eventgrid event-subscription create  --name es3 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
                --advanced-filter data.blobType StringIn BlockBlob
                --advanced-filter data.url StringBeginsWith https://myaccount.blob.core.windows.net
        - name: Create a new event subscription for an Azure subscription, with a filter specifying a subject prefix.
          text: |
            az eventgrid event-subscription create --name es4 \\
                --source-resource-id /subscriptions/{SubID} \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
                --subject-begins-with mysubject_prefix
        - name: Create a new event subscription for a resource group, with a filter specifying a subject suffix.
          text: |
            az eventgrid event-subscription create --name es5 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
                --subject-ends-with mysubject_suffix
        - name: Create a new event subscription for an Azure subscription, using default filters, and an EventHub as a destination.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id /subscriptions/{SubID} \\
                --endpoint-type eventhub \\
                --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.EventHub/namespaces/n1/eventhubs/EH1
        - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure Storage queue as a destination.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id /subscriptions/{SubID} \\
                --endpoint-type storagequeue \\
                --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/queueservices/default/queues/q1
        - name: Create a new event subscription for an Azure subscription, using default filters, and an Azure ServiceBusQueue as a destination.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id /subscriptions/{SubID} \\
                --endpoint-type servicebusqueue \\
                --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.ServiceBus/namespaces/ns1/queues/queue1

        - name: Create a new event subscription for an Event Grid domain, using default filters, and CloudEventV01 as the delivery schema.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1 \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
                --event-delivery-schema cloudeventv01schema
        - name: Create a new event subscription for a storage account, with a deadletter destination and custom retry policy of maximum 10 delivery attempts and an Event TTL of 2 hours (whichever happens earlier).
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/s1" \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code \\
                --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/s2/blobServices/default/containers/blobcontainer1 \\
                --max-delivery-attempts 10 --event-ttl 120
        - name: Create a new event subscription for a domain topic.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/t1" \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Create a new event subscription (for a storage account) with an expiration date.
          text: |
            az eventgrid event-subscription create --name es2 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/sa1" \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
                --expiration-date "2018-10-31"
    """
helps['eventgrid event-subscription update'] = """
    type: command
    short-summary: Update an event subscription.
    parameters:
        - name: --source-resource-id
          short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be updated.
          long-summary: |
            Usage:                      --source-resource-id Azure-Resource-ID
            For Azure subscription:     --source-resource-id /subscriptions/{SubID}
            For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
            For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
            For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
            For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
            For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
        - name: --endpoint-type
          short-summary: The type of the destination endpoint.
    examples:
        - name: Update an event subscription for an Event Grid topic to specify a new endpoint.
          text: |
            az eventgrid event-subscription update --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1 \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Update an event subscription for an Azure subscription to specify a new subject-ends-with filter.
          text: |
            az eventgrid event-subscription update --name es2 \\
                --source-resource-id /subscriptions/{SubID} \\
                --subject-ends-with .jpg
        - name: Update an event subscription for a resource group to specify a new endpoint and a new subject-ends-with filter.
          text: |
            az eventgrid event-subscription update --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG} \\
                --subject-ends-with .png \\
                --endpoint https://contoso.azurewebsites.net/api/f1?code=code
        - name: Update an event subscription for a storage account to specify a new list of included event types.
          text: |
            az eventgrid event-subscription update --name es3 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob" \\
                --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
        - name: Update an event subscription for a storage account, to include a deadletter destination.
          text: |
            az eventgrid event-subscription update --name es2 \\
                --source-resource-id "/subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob" \\
                --deadletter-endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.Storage/storageAccounts/sa1/blobServices/default/containers/blobcontainer1
    """
helps['eventgrid event-subscription delete'] = """
    type: command
    short-summary: Delete an event subscription.
    parameters:
        - name: --source-resource-id
          short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be deleted.
          long-summary: |
            Usage:                      --source-resource-id Azure-Resource-ID
            For Azure subscription:     --source-resource-id /subscriptions/{SubID}
            For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
            For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
            For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
            For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
            For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
    examples:
        - name: Delete an event subscription for an Event Grid topic.
          text: |
            az eventgrid event-subscription delete --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
        - name: Delete an event subscription for an Event Grid domain topic.
          text: |
            az eventgrid event-subscription delete --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1/topics/topic1
        - name: Delete an event subscription for an Event Grid domain.
          text: |
            az eventgrid event-subscription delete --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/domain1
        - name: Delete an event subscription for an Azure subscription.
          text: |
            az eventgrid event-subscription delete --name es2 \\
                --source-resource-id /subscriptions/{SubID}
        - name: Delete an event subscription for a resource group.
          text: |
            az eventgrid event-subscription delete --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
        - name: Delete an event subscription for a storage account.
          text: |
            az eventgrid event-subscription delete --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/microsoft.storage/storageaccounts/kalsegblob
    """
helps['eventgrid event-subscription list'] = """
    type: command
    short-summary: List event subscriptions.
    long-summary: |
        Event Grid supports both regional and global event subscriptions: Event subscriptions on regional resources (such as Storage accounts or Event Grid topics) are regional, while event subscriptions on global resources (such as an Azure subscription or resource group) are global.
        Hence, you can list event subscriptions in a few different ways:
        1. To list by the resource ID of the resource whose event subscriptions you want to list, specify the --source-resource-id parameter. No other parameters must be specified.
        2. To list by a topic-type (e.g. storage accounts), specify the --topic-type parameter along with --location (e.g. "westus2") parameter. For global topic types (e.g. "Microsoft.Resources.Subscriptions"), specify the location value as "global".
        3. To list all event subscriptions in a region (across all topic types), specify only the --location parameter.
        4. For both #2 and #3 above, to filter only by a resource group, you can additionally specify the --resource-group parameter.
    parameters:
        - name: --topic-type-name
          short-summary: Name of the topic-type whose event subscriptions need to be listed. When this is specified, you must also specify --location.
          long-summary: |
            Example 1: List all Storage event subscriptions in WestUS2
                --resource-group TestRG --topic-type-name Microsoft.Storage.StorageAccounts --location westus2
            Example 2: List all event subscriptions on Azure subscriptions
                --topic-type-name Microsoft.Resources.Subscriptions --location global
        - name: --source-resource-id
          short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be listed.
          long-summary: |
            Usage:                      --source-resource-id Azure-Resource-ID
            For Azure subscription:     --source-resource-id /subscriptions/{SubID}
            For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
            For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
            For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
            For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
            For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
    examples:
        - name: List all event subscriptions created for an Event Grid topic.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/topics/topic1
        - name: List all event subscriptions created for a storage account.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.Storage/storageaccounts/kalsegblob
        - name: List all event subscriptions created for an Azure subscription.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}
        - name: List all event subscriptions created for a resource group.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}
        - name: List all event subscriptions for an Event Grid domain.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1
        - name: List all event subscriptions for an Event Grid domain topic.
          text: |
            az eventgrid event-subscription list --source-resource-id /subscriptions/{SubID}/resourceGroups/{RG}/providers/Microsoft.EventGrid/domains/d1/topics/topic1
        - name: List all Storage event subscriptions (under the currently selected Azure subscription) in westus2.
          text: |
            az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2
        - name: List all Storage event subscriptions (under the given resource group) in westus2.
          text: |
            az eventgrid event-subscription list --topic-type Microsoft.Storage.StorageAccounts --location westus2 --resource-group {RG}
        - name: List all regional or global event subscriptions (under the currently selected Azure subscription).
          text: |
            az eventgrid event-subscription list --location westus2
            az eventgrid event-subscription list --location global
        - name: List all regional or global event subscriptions under a specified resource group.
          text: |
            az eventgrid event-subscription list --location westus2 --resource-group {RG}
            az eventgrid event-subscription list --location global --resource-group {RG}
    """
helps['eventgrid event-subscription show'] = """
    type: command
    short-summary: Get the details of an event subscription.
    parameters:
        - name: --source-resource-id
          short-summary: Fully qualified identifier of the Azure resource whose event subscription needs to be shown.
          long-summary: |
            Usage:                      --source-resource-id Azure-Resource-ID
            For Azure subscription:     --source-resource-id /subscriptions/{SubID}
            For resource group:         --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
            For EventGrid topic:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/t1
            For storage account:        --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.Storage/storageaccounts/sa1
            For EventGrid domain:       --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
            For EventGrid domain topic: --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/domains/d1/topics/t1
    examples:
        - name: Show the details of an event subscription for an Event Grid topic.
          text: |
            az eventgrid event-subscription show --name es1 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/Microsoft.EventGrid/topics/topic1
        - name: Show the details of an event subscription for an Azure subscription.
          text: |
            az eventgrid event-subscription show --name es2 \\
                --source-resource-id /subscriptions/{SubID}
        - name: Show the details of an event subscription for a resource group.
          text: |
            az eventgrid event-subscription show --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1
        - name: Show the details of an event subscription for a storage account.
          text: |
            az eventgrid event-subscription show --name es3 \\
                --source-resource-id /subscriptions/{SubID}/resourceGroups/rg1/providers/microsoft.storage/storageaccounts/kalsegblob
    """
helps['eventgrid topic-type'] = """
    type: group
    short-summary: Get details for topic types.
    """
helps['eventgrid topic-type list'] = """
    type: command
    short-summary: List registered topic types.
    """
helps['eventgrid topic-type show'] = """
    type: command
    short-summary: Get the details for a topic type.
    """
helps['eventgrid topic-type list-event-types'] = """
    type: command
    short-summary: List the event types supported by a topic type.
    """
