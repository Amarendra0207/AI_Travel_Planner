"""
Generate architecture diagram for AI Trip Planner
"""

import graphviz

def create_architecture_diagram():
    # Create a new Graphviz object
    dot = graphviz.Digraph(comment='AI Trip Planner Architecture')
    dot.attr(rankdir='TB')

    # Frontend Layer
    with dot.subgraph(name='cluster_0') as c:
        c.attr(label='Frontend Layer')
        c.node('A', 'Streamlit Web UI\nstreamlit_app.py')
        c.node('B', 'FastAPI Backend\nmain.py')
        c.edge('A', 'B', 'HTTP Requests')

    # Core Components
    with dot.subgraph(name='cluster_1') as c:
        c.attr(label='Core Components')
        c.node('C', 'Graph Builder\nagentic_workflow.py')
        c.node('E', 'LangChain Agent')
        c.node('F', 'Model Loader\nmodel_loaders.py')
        c.node('G', 'System Prompts\nprompt.py')
        c.edge('E', 'F', 'Loads')
        c.edge('E', 'G', 'Uses')

    # Tools Layer
    with dot.subgraph(name='cluster_2') as c:
        c.attr(label='Tools Layer')
        tools = {
            'T1': 'Weather Info Tool',
            'T2': 'Place Search Tool',
            'T3': 'Expense Calculator Tool',
            'T4': 'Currency Conversion Tool',
            'T5': 'Distance Calculator Tool',
            'T6': 'Arithmetic Operations Tool'
        }
        for key, value in tools.items():
            c.node(key, value)

    # External Services
    with dot.subgraph(name='cluster_3') as c:
        c.attr(label='External Services')
        services = {
            'S1': 'OpenWeatherMap API',
            'S2': 'Tavily Search API',
            'S3': 'Exchange Rate API',
            'S4': 'OpenRouteService API'
        }
        for key, value in services.items():
            c.node(key, value)

    # Utilities Layer
    with dot.subgraph(name='cluster_4') as c:
        c.attr(label='Utilities')
        utils = {
            'U1': 'Weather Info',
            'U2': 'Place Info Search',
            'U3': 'Expense Calculator',
            'U4': 'Currency Converter',
            'U5': 'Distance Calculator',
            'U6': 'Config Loaders',
            'U7': 'Word Document Exporter'
        }
        for key, value in utils.items():
            c.node(key, value)

    # Connect components
    dot.edge('B', 'C', 'Invokes')
    dot.edge('C', 'E', 'Uses')
    dot.edge('T1', 'S1', 'API Calls')
    dot.edge('T2', 'S2', 'API Calls')
    dot.edge('T4', 'S3', 'API Calls')
    dot.edge('T5', 'S4', 'API Calls')

    # Connect Tools to Utilities
    tool_util_mapping = {
        'T1': 'U1',
        'T2': 'U2',
        'T3': 'U3',
        'T4': 'U4',
        'T5': 'U5'
    }
    for tool, util in tool_util_mapping.items():
        dot.edge(tool, util, 'Uses')

    # Save the diagram
    dot.render('architecture_diagram', format='png', cleanup=True)
    print("Architecture diagram has been generated as 'architecture_diagram.png'")

if __name__ == "__main__":
    create_architecture_diagram()