## https://serper.dev/
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, tool
from langchain_community.tools import DuckDuckGoSearchRun


SERPER_API_KEY = os.getenv('SERPER_API_KEY', 'b329af96cd99860c7ca6b6d57c3204497db48307')


# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# inititlaize the tool for internet searching capabilities
serpertool = SerperDevTool()



@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)
