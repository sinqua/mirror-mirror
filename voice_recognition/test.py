import dialogflow_v2 as dialogflow
session_client = dialogflow.SessionsClient()

session = session_client.session_path('neon-slate-274323', '123456789')
print('Session path: {}\n'.format(session))

texts = ['이름이 뭐야?', '너는 누구니?']
for text in texts:
    text_input = dialogflow.types.TextInput(
    text=text, language_code='ko-KR')

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
                            session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
                response.query_result.fulfillment_text))
