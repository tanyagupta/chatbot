def detect_intent_knowledge(project_id, session_id, language_code,
                            knowledge_base_id, texts):
    """Returns the result of detect intent with querying Knowledge Connector.

    Args:
    project_id: The GCP project linked with the agent you are going to query.
    session_id: Id of the session, using the same `session_id` between requests
              allows continuation of the conversation.
    language_code: Language of the queries.
    knowledge_base_id: The Knowledge base's id to query against.
    texts: A list of text queries to send.
    """
    import dialogflow_v2beta1 as dialogflow
    session_client = dialogflow.SessionsClient()

    session_path = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session_path))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        knowledge_base_path = dialogflow.knowledge_bases_client \
            .KnowledgeBasesClient \
            .knowledge_base_path(project_id, knowledge_base_id)

        query_params = dialogflow.types.QueryParameters(
            knowledge_base_names=[knowledge_base_path])

        response = session_client.detect_intent(
            session=session_path, query_input=query_input,
            query_params=query_params)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        print('Knowledge results:')
        knowledge_answers = response.query_result.knowledge_answers
        for answers in knowledge_answers.answers:
            print(' - Answer: {}'.format(answers.answer))
            print(' - Confidence: {}'.format(
                answers.match_confidence))

if __name__ == '__main__':
    project_id="sunshine-hund"
    session_id="123456789"
    texts=["How many justices are on the Supreme Court?","Who is the President of the United States"]
    knowledge_base_id="ODkwMDkyMjY1OTgyMzQxOTM5Mg"
    language_code="en-US"
    detect_intent_knowledge(project_id, session_id, language_code,knowledge_base_id, texts)
