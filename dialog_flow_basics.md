## Dialogflow ES basics
* A Dialogflow agent is a virtual agent that handles conversations with your end-users.
* An intent categorizes an end-user's intention for one conversation turn.
* A basic intent contains training phrases, action (for each intent), parameters and responses

### Integration vs. API
#### Integration
Dialogflow integrates with many popular conversation platforms and if an integration is used, direct end-user interactions are handled.
When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define.
* Each intent has a setting to enable fulfillment.
* If an intent requires some action by your system or a dynamic response, you should enable fulfillment for the intent.
* If an intent without fulfillment enabled is matched, Dialogflow uses the static response you defined for the intent.
* When an intent with fulfillment enabled is matched, Dialogflow sends a request to the selected webhook service with information about the matched intent. The system can perform any required actions and respond to Dialogflow with information for how to proceed.

The resulting flow is as follows:
* The end-user types or speaks an expression.
* Dialogflow matches the end-user expression to an intent and extracts parameters.
* Dialogflow sends a webhook request message to the webhook service which performs the action and then sends a webhook response message to Dialogflow which sends the response to the end-user.
* The end-user sees or hears the response.

#### API
Without an integration, the programmer has to write the code  that interacts with both the end user and the Diaglogflow API
* The end-user types or speaks an expression which is sent to Dialogflow in a detect intent request message.
* This message contains information about the matched intent, the action, the parameters, and the response defined for the intent.
* The service performs actions as needed, like database queries or external API calls.
* The service sends a response to the end-user.

### Editions
* __Dialogflow Trial Edition__	A free edition that provides most of the features of the standard ES agent type. It offers limited quota and support by community and e-mail. This edition is suitable to experiment with Dialogflow.
* __Dialogflow ES Edition__	The Dialogflow Essentials (ES) Edition is a pay-as-you-go edition that provides the standard ES agent type. The Essentials Edition offers production-ready quotas and support from Google Cloud support.
* __Dialogflow CX Edition__	The Dialogflow Customer Experience (CX) Edition is a pay-as-you-go edition that provides the advanced CX agent type. The CX Edition offers production-ready quotas and support from Google Cloud support.

## Getting started links
* The Google Cloud Console (visit documentation, open console) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products.
* You use the Google Cloud Console to set up and manage Dialogflow resource
* To use services provided by Google Cloud, you must create a project.
[Google Cloud Documentation](https://support.google.com/cloud/answer/3465889?hl=en&ref_topic=3340599)
[Open GCC console](https://console.cloud.google.com/?_ga=2.252287552.83937720.1604759988-1790567636.1602529352)
[Dialogflow ES Console Documentation](https://cloud.google.com/dialogflow/docs/console)
[Open Dialogflow ES Console](https://dialogflow.cloud.google.com/) this will create a basic starter agent but only for use with an integration (and not the API)
[Quickstart Setup](https://cloud.google.com/dialogflow/es/docs/quick/setup)
