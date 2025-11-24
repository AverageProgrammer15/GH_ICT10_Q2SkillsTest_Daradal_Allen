from pyscript import document, display


club_data = {
    "Math Club":{
        "desc":"Math Club focuses on problem-solving, competitions, and tutoring.",
        "meet_time":"Wednesdays 3:00-4:00 PM",
        "location":"Room 101",
        "club_mod":"Mr. Smith",
        "num_of_mem":"25"
    },
    "Social Studies Club":{
        "desc":"Social Studies Club explores history, current events, and civic engagement.",
        "meet_time":"Fridays 2:30-3:30 PM",
        "location":"Room 202",
        "club_mod":"Ms. Johnson",
        "num_of_mem":"18"
    },
    "Glee Club":{
        "desc":"Glee Club is for students who love singing and performing.",
        "meet_time":"Mondays 4:00-5:00 PM",
        "location":"Music Room",
        "club_mod":"Mr. Lee",
        "num_of_mem":"30"
    }
}

def display_data(e):
    grab_value = document.getElementById("choices").value
    subject_data = club_data[grab_value]

    document.getElementById("output").innerHTML = ""

    display(f"Subject: {grab_value}", target="output")
    display(f"Description: {subject_data['desc']}", target="output")
    display(f"Meeting Time: {subject_data['meet_time']}", target="output")
    display(f"Location: {subject_data['location']}", target="output")
    display(f"Club Moderator: {subject_data['club_mod']}", target="output")
    display(f"Number of Members: {subject_data['num_of_mem']}", target="output")



