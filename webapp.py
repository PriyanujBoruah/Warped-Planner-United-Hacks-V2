import streamlit as st
import google.generativeai as palm
import pandas as pd
import datetime
import random



palm.configure(api_key = "INSERT API KEY")







SUBJECT_UG_DS = ['Data Types', 'Data Exploration', 'Data Visualization', 'Linear algebra', 'Calculus', 'Probability', 'Statistics',
                 'Programming and Software Engineering', 'Data Wrangling and Preprocessing', 'Machine Learning Algorithms',
                 'Deep Learning and Neural Networks', 'Natural Language Processing', 'Computer Vision', 'Generative Models',
                 'Big Data and Distributed Computing', 'Data mining', 'Seb Scraping', 'Sentiment Analysis', 'Recommender Systems']

SUBJECT_UG_BS = ['Business Ethics', 'Business Communication', 'Algebra', 'calculus', 'Probability', 'Data Analysis', 'Accounting and Finance',
                 'Marketing and Sales', 'Consumer Behavior', 'Market research', 'Sales management', 'Business Law', 'Organizational Behavior',
                 'Information Technology', 'Database Management', 'E-Commerce', 'Cybersecurity', 'Human Resources', 'Project Management', 'Entrepreneurship',
                 'Microeconomics', 'Macroeconomics', 'Supply and Demand', 'Market Structures', 'Fiscal and Monetary Policies', 'International Business']

SUBJECT_UG_CS = ['Programming Fundamentals', 'Discrete Mathematics', 'Digital Logic Design', 'Object-Oriented Programming',
                 'Data Structures and Algorithms', 'Computer Organization and Architecture', 'Database Systems', 'Operating Systems',
                 'Software Engineering', 'Web Development', 'Computer Networks', 'Artificial Intelligence', 'Theory of Computation',
                 'Compiler Design', 'Data Mining and Machine Learning', 'Cloud Computing', 'Distributed Systems']

SUBJECT_UG_MD = ['Human Anatomy and Physiology', 'Biochemistry', 'Molecular Biology', 'Health and Society', 'Microbiology',
                 'Immunology', 'Pharmacology', 'Therapeutics', 'Research Methods and Statistics', 'Human Genetics and Genomics',
                 'Health Informatics and Technology', 'Health Education and Communication',
                 'Health Law and Ethics', 'Health Management and Leadership']

SUBJECT_UG_PE = ['Physics I (Mechanics, Kinematics and Dynamics)', 'Chemistry I (Atomic Structure, Chemical Bonding and Molecular Geometry)',
                 'Calculus I (Limits, Continuity and Derivatives)', 'Engineering Fundamentals', 'Physics II (Light, Optics, Electricity and Magnetism)',
                 'Chemistry II (Thermodynamics, Chemical Kinetics, Equilibrium, Electro, Nuclear and Organic Chemistry)',
                 'Calculus II (Integration, Improper Integrals, Infinite, Power and Taylor Series)', 'Engineering Mechanics',
                 'Physics III (Modern Physics, Quantum Mechanics, Atomic, Molecular, Nuclear, Particle Physics)',
                 'Differential Equations (Linear, First-order and Second-order)', 'Linear Algebra', 'Engineering Materials',
                 'Numerical Methods', 'Probability and Statistics', 'Engineering Thermodynamics', 'Fluid and Solid Mechanics',
                 'Heat and Mass Transfer', 'Semi-Conductors', 'Microprocessors']

SUBJECT_UG_SC = ['Sociology', 'Psychology', 'Anthropology', 'History', 'Political Science', 'Economics', 'Research Methods and Statistics',
                 'Social Psychology', 'Criminology','Human Geography', 'Public Administration', 'Urban Sociology']

SUBJECT_UG_AH = ['Literature and Language', 'Art History', 'World Languages and Cultures', 'Music History', 'Philosophy and Ethics',
                 'World History and Civilization', 'Creative Writing', 'Comparative Literature', 'Film Studies', 'Theater Arts', 
                 'Religious Studies', 'Fine Arts']

SUBJECT_UG_MA = ['Calculus I (Limits, Continuity and Derivatives,)', 'Linear Algebra I (Matrices, Determinants and Vector Spaces)', 'Discrete Mathematics', 'Introduction to Programming',
                 'Calculus II (Integration, Improper Integrals, Infinite, Power and Taylor Series)', 'Linear Algebra II (Orthogonality, Inner Product Spaces and Gram-Schmidt Process)',
                 'Abstract Algebra', 'Data Structures and Algorithms', 'Calculus III (Vectors, Partial Derivatives, Chain Rule, Maxima and Minima, Stokes Theorem)',
                 'Differential Equations (Linear, First-order and Second-order)', 'Number Theory', 'Probability and Statistics', 'Real Analysis',
                 'Complex Analysis', 'Numerical Analysis', "logic, combinatorics and geometry"]


UG = {'Data Science' : SUBJECT_UG_DS,
      'Business' : SUBJECT_UG_BS,
      'Computer Science' : SUBJECT_UG_CS,
      'Health' : SUBJECT_UG_MD,
      'Physical Science and Engineering' : SUBJECT_UG_PE,
      'Social Sciences' : SUBJECT_UG_SC,
      'Art and Humanities' : SUBJECT_UG_AH,
      'Mathematics' : SUBJECT_UG_MA}


SUBJECT_PG_MS = ["MS in Finance",
    "MS in Business Administration",
    "MS in Economics",
    "MS in Computer Science",
    "MS in Information Technology",
    "MS in Industrial Engineering",
    "MS in Counseling",
    "MS in Physician Assistant Studies",
    "MS in Medical Biochemistry",
    "MS in Geoinformatics",
    "MS in Biotechnology",
    "MS in Data Science",
    "MS in Environmental Science",
    "MS in Pharmacy",
    "MS in Psychology",
    "MS in Statistics",
    "MS in Aerospace Engineering",
    "MS in Chemistry",
    "MS in Physics",
    "MS in Education",
    "MS in Biomedical Engineering",
    "MS in Nanotechnology",
    "MS in Astronomy",
    "MS in Forensic Science",
    "MS in Nutrition",
    "MS in Public Health",
    "MS in Mathematics",
    "MS in Robotics",
    "MS in Sociology",
    "MS in Zoology"] #30


SUBJECT_PG_MA = ["MA in English",
    "MA in History",
    "MA in Political Science",
    "MA in Sociology",
    "MA in Economics",
    "MA in Public Policy",
    "MA in Dance",
    "MA in Home Science",
    "MA in Astrology",
    "MA in Fine Arts",
    "MA in Philosophy",
    "MA in Psychology",
    "MA in Journalism",
    "MA in Linguistics",
    "MA in Music",
    "MA in Anthropology",
    "MA in International Relations",
    "MA in Social Work",
    "MA in Education",
    "MA in Creative Writing",
    ] #20


SUBJECT_PG_MCom = ["M.Com in Finance",
    "M.Com in Business Administration",
    "M.Com in Economics",
    "M.Com in Computer Applications",
    "M.Com in Accountancy",
    "M.Com in Accounting and Finance",
    "M.Com in Business Management",
    "M.Com in Marketing",
    "M.Com in Banking and Finance",
    "M.Com in Financial Management",
    "M.Com in e-Commerce",
    "M.Com in Taxation",
    "M.Com in Finance & Controls",
    "M.Com in Statistics",
    "M.Com in International Business",
    "M.Com in Human Resource Management",
    "M.Com in Co-operative Management",
    "M.Com in Rural Development",
    "M.Com in Insurance Management",
    "M.Com in Corporate Secretaryship"] #20


SUBJECT_PG_MBA = ["MBA in Entrepreneurship",
    "MBA in Financial Management",
    "MBA in Operations Management",
    "MBA in Sustainability",
    "MBA in Human Resources Management",
    "MBA in Digital Transformation",
    "MBA in Marketing Management",
    "MBA in Business Analytics",
    "MBA in Logistics and Supply Chain Management",
    "MBA in Business Law",
    "MBA in International Business",
    "MBA in Healthcare Management",
    "MBA in Entrepreneurship",
    "MBA in Finance and Accounting",
    "MBA in E-Commerce",
    "MBA in Project Management",
    "MBA in Media and Entertainment",
    "MBA in Agribusiness",
    "MBA in Sports Management",
    "MBA in Tourism and Hospitality"] #20


SUBJECT_PG_MCA = ["MCA in Data Science and Analytics",
    "MCA in Software Engineering",
    "MCA in Artificial Intelligence and Machine Learning",
    "MCA in Database Management Systems",
    "MCA in Web Development and Technologies",
    "MCA in Cybersecurity",
    "MCA in Mobile Application Development",
    "MCA in Information Technology",
    "MCA in Computer Applications",
    "MCA in Cloud Computing",
    "MCA in Cloud Technology and Information Security",
    "MCA in Internet of Things",
    "MCA in Big Data Analytics",
    "MCA in Blockchain Technology",
    "MCA in Artificial Neural Networks",
    "MCA in Software Testing and Quality Assurance",
    "MCA in Embedded Systems",
    "MCA in Game Development",
    "MCA in Multimedia and Animation",
    "MCA in Bioinformatics"] #20


SUBJECT_PG_MTech = ["MTech in Data Science and Analytics",
    "MTech in Software Engineering",
    "MTech in Artificial Intelligence and Machine Learning",
    "MTech in Cybersecurity",
    "MTech in Cloud Computing",
    "MTech in Internet of Things",
    "MTech in Biotechnology",
    "MTech in Nanotechnology",
    "MTech in Robotics",
    "MTech in Renewable Energy",
    "MTech in Communication Systems",
    "MTech in Power Systems",
    "MTech in Structural Engineering",
    "MTech in Thermal Engineering",
    "MTech in VLSI Design",
    "MTech in Machine Design",
    "MTech in Manufacturing Engineering",
    "MTech in Transportation Engineering",
    "MTech in Water Resources Engineering",
    "MTech in Geotechnical Engineering"] #20

PG = {'Master of Science (MS)' : SUBJECT_PG_MS,
      'Master of Arts (MA)' : SUBJECT_PG_MA,
      'Master of Commerce (M.Com)' : SUBJECT_PG_MCom,
      'Master of Business Administration (MBA)' : SUBJECT_PG_MBA,
      'Master of Computer Application (MCA)' : SUBJECT_PG_MCA,
      'Master of Technology (MTech)' : SUBJECT_PG_MTech}






### D A S H B O A R D ###




with st.sidebar:
    st.image('360_F_406919447_kAcC5gdh1rpYlVxwMfHtUTGf24PUYSq8__1_-removebg-preview.png')
    category = st.selectbox(
    'Select your most suitable role',
    ('Student (School)','Student (Undergraduate)', 'Student (Postgraduate)', 'Researcher (Doctorate)', 'Professional'), #'Student (School)', 'Researcher (Doctorate)' and 'Professional' are not included in the prototype
    index=None, placeholder="Role not selected")




    mode = st.radio(
        "AI Model : ",
        [":rainbow[Google PaLM 2]"],
        captions = ["LLM"])

    if mode == ':rainbow[AI Mode]':
        st.write(':blue[AI Mode ON]')
    elif mode == 'User Input':
        st.write("Manual Input Enabled")




    if category == "Student (School)":
        grade = st.slider('Grade : ', 1, 12, 8)
        st.write("You are currently in Grade ", grade)
    elif category == "Student (Undergraduate)":
        subject_UG = st.selectbox(
        'Discipline',
        ('Data Science','Business', 'Computer Science', 'Health', 'Physical Science and Engineering',
        'Social Sciences', 'Art and Humanities', 'Mathematics'),
        index=None, placeholder="---Select Discipline---"
        )
    elif category == "Student (Postgraduate)":
        type_PG = st.selectbox(
        'Degree Type',
        ('Master of Science (MS)', 'Master of Arts (MA)', 'Master of Commerce (M.Com)', 'Master of Business Administration (MBA)',
         'Master of Computer Application (MCA)', 'Master of Technology (MTech)'),
        index=None, placeholder="---Select Degree---"
        )


    ai_button = st.button(':rainbow[RUN AI]')



st.title("Warp Planner")
st.subheader(":violet[_The AI powered study recommender._]")
if category == "Student (Undergraduate)":
#####

#####

    if subject_UG:

        sub_select = st.multiselect(
            'COMPLETED COURSES/TOPICS',
            UG.get(subject_UG),
            [])
        total_no_of_sub = len(UG.get(subject_UG))
        no_of_sub_select = len(sub_select)


        UG_STR = '['
        for micro_sub in UG.get(subject_UG):
            if micro_sub == UG.get(subject_UG)[-1]:
                UG_STR += micro_sub + ']'
            else:
                UG_STR += micro_sub + ', '

        print(UG_STR)


        if ai_button:
            completion = (no_of_sub_select / total_no_of_sub)

            if completion < 0.25:
                comp1 = ["Keep going! You've laid the foundation, now build upon it brick by brick.", "Every step forward, no matter how small, is a victory. Keep taking those steps.",
                         "The beginning is always the hardest part. Don't give up now, you're on the right track!", "Believe in yourself and your ability to achieve great things. You've got this!"]
                comp1_out = random.choice(comp1)
                st.subheader(f":violet[{comp1_out}]")
            
            elif completion >= 0.25 and completion < 0.5:
                comp2 = ["Halfway there! Remember, the journey of a thousand miles begins with a single step.", "You're making progress, even if it doesn't feel like it. Keep pushing forward!",
                         "Don't let setbacks discourage you. They're just part of the process. Learn from them and keep moving.", "Take a moment to celebrate how far you've come. Then get back to it and finish strong!"]
                comp2_out = random.choice(comp2)
                st.subheader(f":violet[{comp2_out}]")
            
            elif completion >= 0.5 and completion < 0.75:
                comp3 = ["You're in the home stretch! Stay focused and push through, you're almost there.", "Don't give up now, the finish line is in sight!",
                         "Remember why you started this journey in the first place. Let that be your motivation to keep going.", "You've come so far, don't let anything stop you now!"]
                comp3_out = random.choice(comp3)
                st.subheader(f":violet[{comp3_out}")
            
            elif completion >= 0.75 and completion < 1:
                comp4 = ["Just a little more! You've come so far, don't give up now. You've got this!", "The end is in sight! Keep your eyes on the prize and don't let anything distract you.",
                         "You're so close to achieving your goal! Give it your all and finish strong.", "Imagine how amazing it will feel to finally reach your goal. It's worth every ounce of effort."]
                comp4_out = random.choice(comp4)
                st.subheader(f":violet[{comp4_out}]")
            
            elif completion == 1:
                comp5 = ["Congratulations! You've reached your goal. Celebrate your accomplishment and keep striving for more.", "You did it! You're proof that anything is possible with hard work and dedication.",
                         "Take some time to reflect on your journey and all that you've learned. Then set your sights on your next goal!", "Never stop believing in yourself and your ability to achieve great things. The sky's the limit!"]
                comp5_out = random.choice(comp5)
                st.subheader(f":violet[{comp5_out}]")
            
            else:
                st.text("Something went wrong. Please refresh.")

            st.progress(completion)
            st.text('Subject Completion Percentage = '+str(completion*100))





        col1, col2 = st.columns(2)

        with col1:
            
            count = 0
            sum = 0
            for each_sub in sub_select:
                subject_gpa = st.number_input(f':violet[Enter Grade for {each_sub}]', step = 1)
                sum += subject_gpa
                count += 1




            recent_sub = st.selectbox(
            "Previous Subject",
            UG.get(subject_UG),
            index=None,
            placeholder="---Select Subject---",
            )
            if ai_button:
                st.text("Next Subject Recommendation")
                response_recent_sub = palm.chat(messages = f"""{UG_STR}. i just completed {recent_sub}, what subject should i do next? answer based on the given list. Maximum response length 30 words.""")

                st.caption(response_recent_sub.last)
            
            next_sub = st.selectbox(
            "Next Subject",
            UG.get(subject_UG),
            index=None,
            placeholder="---Select Subject---",
            )
            if ai_button:
                st.text("Quick Summary")
                response_recent_sub = palm.chat(messages = f"""return a summary about {next_sub} in {subject_UG}. answer within 50 words""")

                st.caption(response_recent_sub.last)
            
            project_check = st.checkbox('Get Project Recommendation')
            
            if project_check:

                with st.container(border = True):
                    response = palm.chat(messages = f"""I have completed {sub_select} as part of my Bachelors degree in {subject_UG}. Recommend some projects to showcase them. Maximum length 50 words""")
                    subject_info = response.last
                    st.subheader(":violet[Some Project Recommendations]")
                    st.caption(subject_info)



        if ai_button:

            with col2:

                full_current_datetime = datetime.datetime.now()
                current_date = full_current_datetime.strftime("%j")
                st.subheader("Day " + current_date, )
                st.subheader(f"{str(366-int(current_date))} Days left", divider='violet')
                try:
                    st.subheader(f":violet[CGPA : {str(float(sum)/float(count))}]")
                except:
                    st.text("Due to some error, CGPA could not be calculated")

                with st.container(border= True):
                    response = palm.chat(messages = f"""{UG_STR}. Define point-wise about the benefit of these courses""")

                    subject_info = response.last
                    st.caption(subject_info)


if category == "Student (Postgraduate)":

    if type_PG:

        PG_degree = st.selectbox(
            'COMPLETED COURSES/TOPICS',
            PG.get(type_PG))
        total_no_of_sub = len(PG.get(type_PG))
        no_of_sub_select = len(PG_degree)


        PG_STR = '['
        for micro_sub in PG.get(type_PG):
            if micro_sub == PG.get(type_PG)[-1]:
                PG_STR += micro_sub + ']'
            else:
                PG_STR += micro_sub + ', '

        print(PG_STR)

        col1, col2 = st.columns(2)

        with col1:

            #PG_subject_no = st.number_input(f':violet[Number of Subjects Completed at {each_sub}]', step = 1)
            all_completed_subjects = st.text_area('Completed Courses (separated by comma(,)', placeholder = '---Enter the Completed Courses---')

            all_completed_subjects_list = all_completed_subjects.split(",")

            subject_button = st.button(':violet[Generate Subject Grade Input]')
            if subject_button:
                sum = 0
                count = 0
                for each_sub_PG in all_completed_subjects_list:
                    subject_gpa = st.number_input(f':violet[Enter Grade for {each_sub_PG}]', step = 1)
                    sum += subject_gpa
                    count += 1



            if ai_button:
                response = palm.chat(messages = f"""I have completed {all_completed_subjects} as part of my {PG_degree}. Define point-wise about the benefit of these courses. Maximum length 100 words""")
                subject_info = response.last
                st.caption(subject_info)
        
        
        with col2:

            PG_subject_no = st.number_input(f':violet[Number of Subjects Completed at {PG_degree}]', step = 1)
            PG_subject_total_no = st.number_input(f':violet[Total Number of Subjects Required for {PG_degree}]', step = 1)

            project_check = st.checkbox('Project Recommendation')
            
            if ai_button:

                full_current_datetime = datetime.datetime.now()
                current_date = full_current_datetime.strftime("%j")
                st.subheader("Day " + current_date, )
                st.subheader(f":violet[{str(366-int(current_date))} Days left]", divider="violet")

                try:
                    st.subheader(f":violet[CGPA : {str(float(sum)/float(count))}]")
                except:
                    st.text("Due to some error, CGPA could not be calculated")


                try:
                    PG_completion = PG_subject_no / PG_subject_total_no
                    st.progress(PG_completion)
                    st.text('Completion Percentage = '+str(PG_completion*100))
                except:
                    st.text("Due to some error, Subject Completion Rate could not be calculated")



                if project_check:
                    with st.container(border = True):
                        response = palm.chat(messages = f"""I have completed {all_completed_subjects} as part of my {PG_degree}. Recommend some projects to showcase them. Maximum length 50 words""")
                        subject_info = response.last
                        st.subheader(":violet[Some Project Recommendations]")
                        st.caption(subject_info)
