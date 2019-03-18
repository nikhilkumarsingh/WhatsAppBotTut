{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <center>WhatsApp Bot using Twilio and Python (Part-4)</center><br><center><i><u>Making a conversational bot</u></i></center>\n",
    "\n",
    "![](images/1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](images/dialogflow.svg)\n",
    "\n",
    "### 1. Login into [dialogflow console](https://console.dialogflow.com/api-client/#/login)\n",
    "\n",
    "### 2. Create a new agent or import a pre-built agent\n",
    "\n",
    "### 3. From settings page of agent, open the service account of your project in Google Cloud Console\n",
    "\n",
    "![](images/4.png)\n",
    "\n",
    "### 4. Create a new service account for your project. Download private key for the service account in a JSON file\n",
    "\n",
    "\n",
    "### 5. Install Python Client for Dialogflow\n",
    "- [dialogflow-python-client](https://github.com/googleapis/dialogflow-python-client-v2)\n",
    "    ```\n",
    "    pip install dialogflow\n",
    "    ```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.environ[\"GOOGLE_APPLICATION_CREDENTIALS\"] = \"nikubuntu-1-5d7d63a5b8ca.json\"\n",
    "\n",
    "import dialogflow_v2 as dialogflow\n",
    "dialogflow_session_client = dialogflow.SessionsClient()\n",
    "PROJECT_ID = \"nikubuntu-1\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def detect_intent_from_text(text, session_id, language_code='en'):\n",
    "    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)\n",
    "    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)\n",
    "    query_input = dialogflow.types.QueryInput(text=text_input)\n",
    "    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)\n",
    "    return response.query_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = detect_intent_from_text(\"say joke\", 12314)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Worrying works! 90% of the things I worry about never happen.'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.fulfillment_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'jokes.get'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.intent.display_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.intent_detection_confidence"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
