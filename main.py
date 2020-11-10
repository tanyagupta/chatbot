import argparse
import base64
import dialogflow_v2beta1 as dialogflow

KNOWLEDGE_TYPES = ['KNOWLEDGE_TYPE_UNSPECIFIED', 'FAQ', 'EXTRACTIVE_QA']
# Useful source: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dialogflow/cloud-client/document_management.py

def detect_intent_knowledge_from_external_url(project_id, session_id, language_code,knowledge_base_id, texts):
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






def create_knowledge_base(project_id, display_name):
    """Creates a Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        display_name: The display name of the Knowledge base."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    project_path = client.project_path(project_id)

    knowledge_base = dialogflow.types.KnowledgeBase(
        display_name=display_name)

    response = client.create_knowledge_base(project_path, knowledge_base)

    print('Knowledge Base created:\n')
    print('Display Name: {}\n'.format(response.display_name))
    print('Knowledge ID: {}\n'.format(response.name))

def delete_document(project_id,knowledge_base_id,document_id):
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.DocumentsClient()
    name = client.document_path(project_id,knowledge_base_id,document_id)
    response = client.delete_document(name)

def list_documents(project_id,knowledge_base_id):
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.DocumentsClient()
    parent = client.knowledge_base_path(project_id, knowledge_base_id)
    # Iterate over all results
    for element in client.list_documents(parent):
        print(element.name)
        print(element.display_name)
        print(element.mime_type)

        for knowledge_type in element.knowledge_types:
            print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
        # process element
        pass

def readfile(filename):
    file_content_as_string = " "

    try:
        file_handle = open(filename, "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return file_content_as_string
        #print (file_content_as_string)
    except IndexError:
        print ("No file name to read")

def create_document(project_id, knowledge_base_id, display_name, mime_type,
                    knowledge_type, content_uri):
    """Creates a Document.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base.
        display_name: The display name of the Document.
        mime_type: The mime_type of the Document. e.g. text/csv, text/html,
            text/plain, text/pdf etc.
        knowledge_type: The Knowledge type of the Document. e.g. FAQ,
            EXTRACTIVE_QA.
        content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
            http://mypage.com/faq.html."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(project_id,
                                                     knowledge_base_id)

    document = dialogflow.types.Document(
        display_name=display_name, mime_type=mime_type,
        content_uri=content_uri)

    document.knowledge_types.append(
        dialogflow.types.Document.KnowledgeType.Value(knowledge_type))

    response = client.create_document(knowledge_base_path, document)
    print('Waiting for results...')
    document = response.result(timeout=120)
    print('Created Document:')
    print(' - Display Name: {}'.format(document.display_name))
    print(' - Knowledge ID: {}'.format(document.name))
    print(' - MIME Type: {}'.format(document.mime_type))
    for knowledge_type in document.knowledge_types:
        print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
    print(' - Source: {}\n'.format(document.raw_content))



def create_document_from_internal_file(project_id, knowledge_base_id, display_name, mime_type,
                    knowledge_type, rawContent):
    """Creates a Document.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base.
        display_name: The display name of the Document.
        mime_type: The mime_type of the Document. e.g. text/csv, text/html,
            text/plain, text/pdf etc.
        knowledge_type: The Knowledge type of the Document. e.g. FAQ,
            EXTRACTIVE_QA.
        content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
            http://mypage.com/faq.html."""

    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(project_id,knowledge_base_id)
    message_bytes = rawContent.encode('utf-8') #note: tried ascii format before but fails for accents
    document = dialogflow.types.Document(
        display_name=display_name, mime_type='text/csv',raw_content=message_bytes,
        knowledge_types=['FAQ'])

    document.knowledge_types.append(
        dialogflow.types.Document.KnowledgeType.Value(knowledge_type))

    response = client.create_document(knowledge_base_path, document)
    print('Waiting for results...')
    document = response.result(timeout=120)
    print('Created Document:')
    print(' - Display Name: {}'.format(document.display_name))
    print(' - Knowledge ID: {}'.format(document.name))
    print(' - MIME Type: {}'.format(document.mime_type))
    for knowledge_type in document.knowledge_types:
        print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
    print(' - Source: {}\n'.format(document.raw_content))


if __name__ == '__main__':

    project_id="sunshine-hund"
    session_id="123456789"
    texts=["How many justices are on the Supreme Court?","Who is the President of the United States"]
    knowledge_base_id="ODkwMDkyMjY1OTgyMzQxOTM5Mg"
    display_name="Capitals"
    mime_type="text/csv"
    knowledge_type="FAQ"
    document_id="MTY2MDE4NDM4MjY2NTAyNTEyNjQ"
    content_uri="gs://captals/capitals.csv"
    fileBytes  = readfile("capitals.csv")
    language_code="en-US"
    #print(fileBytes)
    create_document_from_internal_file(project_id, knowledge_base_id, display_name, mime_type,knowledge_type, rawContent=fileBytes)
    #detect_intent_knowledge_from_external_url(project_id, session_id, language_code,knowledge_base_id, texts)
    # detect_intent_knowledge(project_id, session_id, language_code,knowledge_base_id, texts)

    #create_document(project_id, knowledge_base_id, display_name, mime_type,knowledge_type, content_uri)
    #create_knowledge_base(project_id, display_name)
    #delete_document(project_id,knowledge_base_id,document_id)
    #list_documents(project_id,knowledge_base_id)
