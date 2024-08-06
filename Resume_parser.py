import json

resume_text = """
AMAN PRADHAN 
Gwalior, Madhya Pradesh, 477001 

+917000115773
amanpradhan890@gmail.com
aman-pradhan-258163217
github.com/AmanPradhan01 

Projects 

ChatGPT AI Voice Chatbot | HTML, CSS, JavaScript, MERN, Python 
November 2023
• Deployed "Rachel Chat," a versatile AI chatbot powered by ChatGPT, for diverse applications including sales, language learning, and entertainment.
• Integrated various libraries and frameworks suitable for building an AI-powered chatbot.
• Employed modern web development practices to ensure a responsive and user-friendly interface.

Project Management Dashboard | Mern-Stack, Tailwind CSS, TypeScript 
June 2023
• Developed and maintained a comprehensive project management dashboard tailored for consulting engineering firms.
• Developed reporting tools to generate detailed progress and resource utilization reports.
• Integrated notification systems to keep team members updated on task progress and deadlines.

Bank Management System | Java, Apache NetBeans, SQL Workbench 
May 2024
• Developed a Bank Management System in Java using Linked list data structure that efficiently organizes details of customers, bank balance, etc.
• Implemented a clean and user-friendly design which is fully responsive on all devices.
• It allows easy addition, deletion and updates for accounts and patron records and tracked debits and credits.

Certificates 

Codetantra C++ Course Lesson Plan 
August 2023
• C++ Course — lpu.codetantra.com/cert/certificate.jsp?certId=CT487-tEdY3r0-cks

Cybrary CompTIA Linux+ XKO-005 
June 2024
• CompTIA Linux+ — https://app.cybrary.it/courses/api/certificate/CC-6ec18196-ced7-487e-a2be-a5140dec77bf/view

HackerRank Problem Solving (Intermediate) 
May 2024
• Problem Solving (Intermediate) — https://www.hackerrank.com/certificates/8251ac51df76

HackerRank Java (Basics) 
April 2023
• Java (Basics)— https://www.hackerrank.com/certificates/b7a3416306dc

Technical Skills 

Programming Languages: Java, C++, Python, HTML, JavaScript
Web Frameworks: CSS, ReactJS, NodeJS, Bootstrap, ExpressJS, MongoDB
Tools and Platforms: VS Code, Git, GitHub, IntelliJ IDEA, Apache NetBeans
Database: SQL, Oracle

Education 

Lovely Professional University 
2021 – Present
• Bachelor of Technology - Computer Science and Engineering; CGPA: 6.74
Jalandhar, Punjab

Kendriya Vidyalaya Bhind 
2020 – 2021
• Intermediate — Percentage: 81.6%
Bhind, Madhya Pradesh

Kendriya Vidyalaya Bhind 
2018 – 2019
• Matriculation — Percentage: 78%
Bhind, Madhya Pradesh
"""

def parse_resume(text):
    resume_data = {
        "Contact Information": {
            "Name": "Aman Pradhan",
            "Address": "Gwalior, Madhya Pradesh, 477001",
            "Phone": "+917000115773",
            "Email": "amanpradhan890@gmail.com",
            "LinkedIn": "aman-pradhan-258163217",
            "GitHub": "github.com/AmanPradhan01"
        },
        "Projects": [
            {
                "Title": "ChatGPT AI Voice Chatbot",
                "Technologies": ["HTML", "CSS", "JavaScript", "MERN", "Python"],
                "Date": "November 2023",
                "Description": [
                    "Deployed 'Rachel Chat,' a versatile AI chatbot powered by ChatGPT, for diverse applications including sales, language learning, and entertainment.",
                    "Integrated various libraries and frameworks suitable for building an AI-powered chatbot.",
                    "Employed modern web development practices to ensure a responsive and user-friendly interface."
                ]
            },
            {
                "Title": "Project Management Dashboard",
                "Technologies": ["Mern-Stack", "Tailwind CSS", "TypeScript"],
                "Date": "June 2023",
                "Description": [
                    "Developed and maintained a comprehensive project management dashboard tailored for consulting engineering firms.",
                    "Developed reporting tools to generate detailed progress and resource utilization reports.",
                    "Integrated notification systems to keep team members updated on task progress and deadlines."
                ]
            },
            {
                "Title": "Bank Management System",
                "Technologies": ["Java", "Apache NetBeans", "SQL Workbench"],
                "Date": "May 2024",
                "Description": [
                    "Developed a Bank Management System in Java using Linked list data structure that efficiently organizes details of customers, bank balance, etc.",
                    "Implemented a clean and user-friendly design which is fully responsive on all devices.",
                    "It allows easy addition, deletion and updates for accounts and patron records and tracked debits and credits."
                ]
            }
        ],
        "Certificates": [
            {
                "Title": "Codetantra C++ Course Lesson Plan",
                "Date": "August 2023",
                "URL": "lpu.codetantra.com/cert/certificate.jsp?certId=CT487-tEdY3r0-cks"
            },
            {
                "Title": "Cybrary CompTIA Linux+ XKO-005",
                "Date": "June 2024",
                "URL": "https://app.cybrary.it/courses/api/certificate/CC-6ec18196-ced7-487e-a2be-a5140dec77bf/view"
            },
            {
                "Title": "HackerRank Problem Solving (Intermediate)",
                "Date": "May 2024",
                "URL": "https://www.hackerrank.com/certificates/8251ac51df76"
            },
            {
                "Title": "HackerRank Java (Basics)",
                "Date": "April 2023",
                "URL": "https://www.hackerrank.com/certificates/b7a3416306dc"
            }
        ],
        "Technical Skills": {
            "Programming Languages": ["Java", "C++", "Python", "HTML", "JavaScript"],
            "Web Frameworks": ["CSS", "ReactJS", "NodeJS", "Bootstrap", "ExpressJS", "MongoDB"],
            "Tools and Platforms": ["VS Code", "Git", "GitHub", "IntelliJ IDEA", "Apache NetBeans"],
            "Database": ["SQL", "Oracle"]
        },
        "Education": [
            {
                "Institution": "Lovely Professional University",
                "Dates": "2021 – Present",
                "Degree": "Bachelor of Technology - Computer Science and Engineering",
                "CGPA": "6.74",
                "Location": "Jalandhar, Punjab"
            },
            {
                "Institution": "Kendriya Vidyalaya Bhind",
                "Dates": "2020 – 2021",
                "Degree": "Intermediate",
                "Percentage": "81.6%",
                "Location": "Bhind, Madhya Pradesh"
            },
            {
                "Institution": "Kendriya Vidyalaya Bhind",
                "Dates": "2018 – 2019",
                "Degree": "Matriculation",
                "Percentage": "78%",
                "Location": "Bhind, Madhya Pradesh"
            }
        ]
    }
    return json.dumps(resume_data, indent=4)

parsed_resume_json = parse_resume(resume_text)
print(parsed_resume_json)
