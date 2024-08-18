from django.shortcuts import render

def agent_list(request):
    # Logic to retrieve and display all agents
    return render(request, 'agents/agent_list.html')

def agent_detail(request, agent_id):
    # Logic to retrieve and display specific agent details
    return render(request, 'agents/agent_detail.html', {'agent_id': agent_id})
