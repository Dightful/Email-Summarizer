from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_email(email_text, sentences_count=4):
    """
    Summarizes the given email text using Sumy.

    Args:
    - email_text (str): The text of the email to summarize.
    - sentences_count (int): The number of sentences to include in the summary.

    Returns:
    - str: The summarized text.
    """
    parser = PlaintextParser.from_string(email_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join(str(sentence) for sentence in summary)

# Example usage
email_text = """
Dear Team,

I wanted to provide a quick update on the project status. We have successfully completed the first phase and are now moving on to the second phase. The initial results are promising, and we are on track to meet our deadlines.

However, we have encountered some challenges with the integration of the new system. The tech team is currently working on resolving these issues, and we should have a solution by the end of the week.

This is important, you are fired.

I also wanted to remind everyone about the upcoming meeting next Monday, where we will discuss the progress and plan the next steps. Please make sure to review the project documentation before the meeting.

Thank you for your hard work and dedication.

Best regards,
Project Manager
"""

summary = summarize_email(email_text)
print(summary)