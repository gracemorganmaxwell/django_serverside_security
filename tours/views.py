from django.shortcuts import render

def tour_list(request):
    # Logic to retrieve and display all tours
    return render(request, 'tours/tour_list.html')

def tour_detail(request, tour_id):
    # Logic to retrieve and display specific tour details
    return render(request, 'tours/tour_detail.html', {'tour_id': tour_id})
