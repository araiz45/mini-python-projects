# String concatination (aka how we put strings together)
# # Suppose we want the string name subscribe_to = ________
# youtuber = "coder " # Youtuber name
# num = 3
#
# # few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
# print(f"Subscribe to {num}")

name = input("Enter Your name : ")
name = name.capitalize()
profession = input("Enter your profession name : ")
profession = profession.lower()
company_pro = input("Do you work for any company (y/n): ")
company_pro = company_pro.lower()
company = input("Enter your company name : " or "none")
company = company.capitalize()
inter_pro = input("Did you complete intermediate (y/n): ")
inter_pro = inter_pro.lower()
inter = input("From Which college did you complete intermediate : " or "none")
inter = inter.capitalize()
b_uni_pro = input("Did you complete your bachelors degree (y/n): ")
b_uni_pro = b_uni_pro.lower()
b_uni = input("From Which University did you do bachelors degree : " or "none")
b_uni = b_uni.capitalize()
b_uni_program = input("In which program did you do bachelors degree : " or "none")
b_uni_program = b_uni_program.capitalize()
b_uni_year = input("In which year did you complete your bachelors degree: ")
m_uni_pro = input("Did you complete your master's degree (y/n) : ")
m_uni_pro = m_uni_pro.lower()
m_uni = input("From which university did complete masters : " or "none")
m_uni = m_uni.capitalize()
m_uni_program = input("In which program did you do masters degree : " or "none")
m_uni_program = m_uni_program.capitalize()
m_uni_year = input("In which year did you complete your masters program : ")
first_company_pro = input("Did you done your first job (y/n) : ")
first_company_pro = first_company_pro.lower()
first_company = input("In Which company did you perform your first job : " or "none")
experience_pro = input("Did you have any years of experience (y/n) : ")
experience_pro = experience_pro.lower()
experience_year = input("How many years of experience do you have : " or "none")
experience_field = input("In which field do you have experience : " or "none")
experience_field = experience_field.lower()

matlib = f"I am {name}, I am a {profession} at {company}. I completed my intermediate from {inter} \n" \
         f"and went to {b_uni} and completed my bachelor degree in {b_uni_program} in {b_uni_year}, I have " \
         f"done my masters degree in {m_uni_program}" \
         f"\nfrom {m_uni} in {m_uni_year} " \
         f"and started job at {first_company}, I have {experience_year} years of exper" \
         f"ience in {experience_field}."


# if company_pro == 'n':
#     matlib = matlib[:39].join(matlib[52:])

print(matlib)




