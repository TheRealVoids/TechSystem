import os

import django

# Setting up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techsystem.settings")
django.setup()

from apps.common.services.pgadmin.models import (
    Category,
    Company,
    Contact,
    ContactDepartment,
    Contract,
    DeliveryCertificate,
    Department,
    Equipment,
    Interaction,
    Opportunity,
    OpportunityProductService,
    OpportunityStage,
    OpportunityStageHistory,
    ProductService,
    Role,
    UserAccount,
    UserRole,
)


def reset_database():
    """Drop all application tables before generating new data."""
    models = [
        Equipment,
        DeliveryCertificate,
        Contract,
        OpportunityProductService,
        ProductService,
        OpportunityStageHistory,
        OpportunityStage,
        Opportunity,
        UserRole,
        UserAccount,
        Role,
        ContactDepartment,
        Department,
        Contact,
        Company,
        Interaction,
        Category,
    ]
    for model in models:
        model.objects.all().delete()

    print("All data deleted")


def populate_database():
    """Fill the database with the initial data provided."""
    # Insert data into Company
    companies = [
        Company(
            nit="123456789",
            name="Tech Innovations",
            industry="Technology",
            address="123 Silicon Valley St.",
            phone="555-1000",
            email="info@techinnovations.com",
            country="USA",
            state="CA",
            creation_date="2015-04-23",
        ),
        Company(
            nit="987654321",
            name="Global Finances",
            industry="Finance",
            address="456 Wall Street",
            phone="555-2000",
            email="contact@globalfinances.com",
            country="USA",
            state="NY",
            creation_date="2010-11-11",
        ),
        Company(
            nit="456123789",
            name="Healthcare Solutions",
            industry="Healthcare",
            address="789 Medway Ave.",
            phone="555-3000",
            email="support@healthsolutions.com",
            country="USA",
            state="TX",
            creation_date="2018-07-30",
        ),
        Company(
            nit="321654987",
            name="Eco Energy",
            industry="Energy",
            address="101 Greenway Blvd.",
            phone="555-4000",
            email="info@ecoenergy.com",
            country="USA",
            state="WA",
            creation_date="2012-05-14",
        ),
        Company(
            nit="654987321",
            name="Retail Giants",
            industry="Retail",
            address="202 Market St.",
            phone="555-5000",
            email="contact@retailgiants.com",
            country="USA",
            state="IL",
            creation_date="2008-09-19",
        ),
        Company(
            nit="789321654",
            name="Auto Innovators",
            industry="Automotive",
            address="303 Motorway Dr.",
            phone="555-6000",
            email="support@autoinnovators.com",
            country="USA",
            state="MI",
            creation_date="2016-03-22",
        ),
        Company(
            nit="147258369",
            name="Foodies Delight",
            industry="Food & Beverage",
            address="404 Culinary Rd.",
            phone="555-7000",
            email="info@foodiesdelight.com",
            country="USA",
            state="CA",
            creation_date="2013-12-05",
        ),
        Company(
            nit="963852741",
            name="Travel Experts",
            industry="Travel",
            address="505 Adventure Ln.",
            phone="555-8000",
            email="contact@travelexperts.com",
            country="USA",
            state="FL",
            creation_date="2011-07-18",
        ),
        Company(
            nit="852741963",
            name="Media Masters",
            industry="Media",
            address="606 Broadcast Ave.",
            phone="555-9000",
            email="info@mediamasters.com",
            country="USA",
            state="NY",
            creation_date="2014-11-30",
        ),
        Company(
            nit="741963852",
            name="Construction Pros",
            industry="Construction",
            address="707 Builder St.",
            phone="555-1001",
            email="support@constructionpros.com",
            country="USA",
            state="TX",
            creation_date="2009-04-25",
        ),
        Company(
            nit="159753486",
            name="Fashion Forward",
            industry="Fashion",
            address="808 Style Blvd.",
            phone="555-2001",
            email="info@fashionforward.com",
            country="USA",
            state="CA",
            creation_date="2017-08-12",
        ),
        Company(
            nit="357951486",
            name="Tech Pioneers",
            industry="Technology",
            address="909 Innovation Dr.",
            phone="555-3001",
            email="contact@techpioneers.com",
            country="USA",
            state="MA",
            creation_date="2019-02-28",
        ),
        Company(
            nit="258963147",
            name="Health First",
            industry="Healthcare",
            address="1010 Wellness Way",
            phone="555-4001",
            email="support@healthfirst.com",
            country="USA",
            state="FL",
            creation_date="2010-06-15",
        ),
        Company(
            nit="654321789",
            name="Finance Gurus",
            industry="Finance",
            address="1111 Money St.",
            phone="555-5001",
            email="info@financegurus.com",
            country="USA",
            state="NY",
            creation_date="2011-10-20",
        ),
        Company(
            nit="789654123",
            name="Green Earth",
            industry="Environmental",
            address="1212 Eco Rd.",
            phone="555-6001",
            email="contact@greenearth.com",
            country="USA",
            state="OR",
            creation_date="2014-03-10",
        ),
        Company(
            nit="321789654",
            name="Logistics Leaders",
            industry="Logistics",
            address="1313 Transport Ave.",
            phone="555-7001",
            email="info@logisticsleaders.com",
            country="USA",
            state="TX",
            creation_date="2012-09-05",
        ),
        Company(
            nit="987321654",
            name="Real Estate Experts",
            industry="Real Estate",
            address="1414 Property Blvd.",
            phone="555-8001",
            email="support@realestateexperts.com",
            country="USA",
            state="CA",
            creation_date="2015-01-25",
        ),
        Company(
            nit="654789321",
            name="Education Innovators",
            industry="Education",
            address="1515 Learning Ln.",
            phone="555-9001",
            email="info@educationinnovators.com",
            country="USA",
            state="NY",
            creation_date="2013-05-30",
        ),
        Company(
            nit="321654988",
            name="Entertainment Hub",
            industry="Entertainment",
            address="1616 Fun St.",
            phone="555-1002",
            email="contact@entertainmenthub.com",
            country="USA",
            state="NV",
            creation_date="2016-11-11",
        ),
        Company(
            nit="789123456",
            name="Sports World",
            industry="Sports",
            address="1717 Athlete Ave.",
            phone="555-2002",
            email="info@sportsworld.com",
            country="USA",
            state="TX",
            creation_date="2017-04-14",
        ),
        Company(
            nit="456789123",
            name="Beauty Bliss",
            industry="Beauty",
            address="1818 Glamour Rd.",
            phone="555-3002",
            email="support@beautybliss.com",
            country="USA",
            state="CA",
            creation_date="2018-08-22",
        ),
        Company(
            nit="123789456",
            name="Automotive Excellence",
            industry="Automotive",
            address="1919 Drive St.",
            phone="555-4002",
            email="info@automotiveexcellence.com",
            country="USA",
            state="MI",
            creation_date="2019-12-01",
        ),
        Company(
            nit="789456123",
            name="Tech Titans",
            industry="Technology",
            address="2020 Future Blvd.",
            phone="555-5002",
            email="contact@techtitans.com",
            country="USA",
            state="CA",
            creation_date="2020-07-07",
        ),
        Company(
            nit="456123788",
            name="Healthcare Heroes",
            industry="Healthcare",
            address="2121 Care St.",
            phone="555-6002",
            email="support@healthcareheroes.com",
            country="USA",
            state="TX",
            creation_date="2021-03-15",
        ),
        Company(
            nit="123456788",
            name="Finance Wizards",
            industry="Finance",
            address="2222 Wealth Rd.",
            phone="555-7002",
            email="info@financewizards.com",
            country="USA",
            state="NY",
            creation_date="2022-11-20",
        ),
    ]
    Company.objects.bulk_create(companies)

    print("Inserted Company data...")

    # Inserting data into Contact
    contacts = [
        Contact(
            contact_id="C1",
            nit=companies[0],
            first_name="John",
            last_name="Doe",
            position="CTO",
            phone="555-1001",
            email="jdoe@techinnovations.com",
            last_interaction_date="2024-10-10",
        ),
        Contact(
            contact_id="C2",
            nit=companies[1],
            first_name="Jane",
            last_name="Smith",
            position="Finance Director",
            phone="555-2001",
            email="jsmith@globalfinances.com",
            last_interaction_date="2024-09-20",
        ),
        Contact(
            contact_id="C3",
            nit=companies[2],
            first_name="Mary",
            last_name="Johnson",
            position="Head of IT",
            phone="555-3001",
            email="mjohnson@healthsolutions.com",
            last_interaction_date="2024-08-15",
        ),
        Contact(
            contact_id="C4",
            nit=companies[3],
            first_name="James",
            last_name="Brown",
            position="CEO",
            phone="555-4001",
            email="jbrown@techinnovations.com",
            last_interaction_date="2024-07-10",
        ),
        Contact(
            contact_id="C5",
            nit=companies[4],
            first_name="Patricia",
            last_name="Garcia",
            position="Marketing Manager",
            phone="555-5001",
            email="pgarcia@globalfinances.com",
            last_interaction_date="2024-06-20",
        ),
        Contact(
            contact_id="C6",
            nit=companies[5],
            first_name="Robert",
            last_name="Martinez",
            position="Sales Director",
            phone="555-6001",
            email="rmartinez@healthsolutions.com",
            last_interaction_date="2024-05-15",
        ),
        Contact(
            contact_id="C7",
            nit=companies[6],
            first_name="Linda",
            last_name="Davis",
            position="HR Manager",
            phone="555-7001",
            email="ldavis@techinnovations.com",
            last_interaction_date="2024-04-10",
        ),
        Contact(
            contact_id="C8",
            nit=companies[7],
            first_name="Michael",
            last_name="Rodriguez",
            position="Operations Manager",
            phone="555-8001",
            email="mrodriguez@globalfinances.com",
            last_interaction_date="2024-03-20",
        ),
        Contact(
            contact_id="C9",
            nit=companies[8],
            first_name="Barbara",
            last_name="Wilson",
            position="Product Manager",
            phone="555-9001",
            email="bwilson@healthsolutions.com",
            last_interaction_date="2024-02-15",
        ),
        Contact(
            contact_id="C10",
            nit=companies[9],
            first_name="William",
            last_name="Lopez",
            position="Chief Engineer",
            phone="555-1002",
            email="wlopez@techinnovations.com",
            last_interaction_date="2024-01-10",
        ),
        Contact(
            contact_id="C11",
            nit=companies[10],
            first_name="Elizabeth",
            last_name="Hernandez",
            position="Chief Scientist",
            phone="555-2002",
            email="ehernandez@globalfinances.com",
            last_interaction_date="2023-12-20",
        ),
        Contact(
            contact_id="C12",
            nit=companies[11],
            first_name="David",
            last_name="King",
            position="Chief Architect",
            phone="555-3002",
            email="dking@healthsolutions.com",
            last_interaction_date="2023-11-15",
        ),
        Contact(
            contact_id="C13",
            nit=companies[12],
            first_name="Susan",
            last_name="Wright",
            position="Chief Designer",
            phone="555-4002",
            email="swright@techinnovations.com",
            last_interaction_date="2023-10-10",
        ),
        Contact(
            contact_id="C14",
            nit=companies[13],
            first_name="Joseph",
            last_name="Green",
            position="Chief Analyst",
            phone="555-5002",
            email="jgreen@globalfinances.com",
            last_interaction_date="2023-09-20",
        ),
        Contact(
            contact_id="C15",
            nit=companies[14],
            first_name="Karen",
            last_name="Adams",
            position="Chief Strategist",
            phone="555-6002",
            email="kadams@healthsolutions.com",
            last_interaction_date="2023-08-15",
        ),
        Contact(
            contact_id="C16",
            nit=companies[15],
            first_name="Charles",
            last_name="Baker",
            position="Chief Consultant",
            phone="555-7002",
            email="cbaker@techinnovations.com",
            last_interaction_date="2023-07-10",
        ),
        Contact(
            contact_id="C17",
            nit=companies[16],
            first_name="Jessica",
            last_name="Nelson",
            position="Chief Advisor",
            phone="555-8002",
            email="jnelson@globalfinances.com",
            last_interaction_date="2023-06-20",
        ),
        Contact(
            contact_id="C18",
            nit=companies[17],
            first_name="Daniel",
            last_name="Carter",
            position="Chief Planner",
            phone="555-9002",
            email="dcarter@healthsolutions.com",
            last_interaction_date="2023-05-15",
        ),
        Contact(
            contact_id="C19",
            nit=companies[18],
            first_name="Nancy",
            last_name="Mitchell",
            position="Chief Auditor",
            phone="555-1003",
            email="nmitchell@techinnovations.com",
            last_interaction_date="2023-04-10",
        ),
        Contact(
            contact_id="C20",
            nit=companies[19],
            first_name="Paul",
            last_name="Perez",
            position="Chief Negotiator",
            phone="555-2003",
            email="pperez@globalfinances.com",
            last_interaction_date="2023-03-20",
        ),
        Contact(
            contact_id="C21",
            nit=companies[20],
            first_name="Lisa",
            last_name="Roberts",
            position="Chief Coordinator",
            phone="555-3003",
            email="lroberts@healthsolutions.com",
            last_interaction_date="2023-02-15",
        ),
        Contact(
            contact_id="C22",
            nit=companies[21],
            first_name="Mark",
            last_name="Turner",
            position="Chief Developer",
            phone="555-4003",
            email="mturner@techinnovations.com",
            last_interaction_date="2023-01-10",
        ),
        Contact(
            contact_id="C23",
            nit=companies[22],
            first_name="Sandra",
            last_name="Phillips",
            position="Chief Researcher",
            phone="555-5003",
            email="sphillips@globalfinances.com",
            last_interaction_date="2022-12-20",
        ),
        Contact(
            contact_id="C24",
            nit=companies[23],
            first_name="George",
            last_name="Campbell",
            position="Chief Investigator",
            phone="555-6003",
            email="gcampbell@healthsolutions.com",
            last_interaction_date="2022-11-15",
        ),
        Contact(
            contact_id="C25",
            nit=companies[24],
            first_name="Betty",
            last_name="Parker",
            position="Chief Examiner",
            phone="555-7003",
            email="bparker@techinnovations.com",
            last_interaction_date="2022-10-10",
        ),
    ]
    Contact.objects.bulk_create(contacts)

    print("Inserted Contact data...")

    # Insert data into Interaction
    interactions = [
        Interaction(
            interaction_id="I1",
            contact_id=contacts[0],
            interaction_date="2024-10-01",
            interaction_type="Email",
            notes="Discussed project requirements and timeline.",
        ),
        Interaction(
            interaction_id="I2",
            contact_id=contacts[1],
            interaction_date="2024-09-15",
            interaction_type="Phone Call",
            notes="Reviewed financial software upgrade proposal.",
        ),
        Interaction(
            interaction_id="I3",
            contact_id=contacts[2],
            interaction_date="2024-08-10",
            interaction_type="Meeting",
            notes="Initial meeting to discuss data integration.",
        ),
        Interaction(
            interaction_id="I4",
            contact_id=contacts[0],
            interaction_date="2024-10-05",
            interaction_type="Meeting",
            notes="Follow-up meeting to discuss project details.",
        ),
        Interaction(
            interaction_id="I5",
            contact_id=contacts[0],
            interaction_date="2024-10-15",
            interaction_type="Phone Call",
            notes="Discussed budget and timeline adjustments.",
        ),
        Interaction(
            interaction_id="I6",
            contact_id=contacts[1],
            interaction_date="2024-09-25",
            interaction_type="Email",
            notes="Sent revised proposal for financial software upgrade.",
        ),
        Interaction(
            interaction_id="I7",
            contact_id=contacts[1],
            interaction_date="2024-10-05",
            interaction_type="Meeting",
            notes="Meeting to finalize contract terms.",
        ),
        Interaction(
            interaction_id="I8",
            contact_id=contacts[2],
            interaction_date="2024-08-20",
            interaction_type="Phone Call",
            notes="Discussed data integration requirements.",
        ),
        Interaction(
            interaction_id="I9",
            contact_id=contacts[2],
            interaction_date="2024-09-01",
            interaction_type="Email",
            notes="Sent initial data integration plan.",
        ),
    ]
    Interaction.objects.bulk_create(interactions)

    print("Inserted Interaction data...")

    # Insert data into Department
    departments = [
        Department(
            department_id="D1",
            department_name="IT",
            description="Handles information technology",
        ),
        Department(
            department_id="D2",
            department_name="Finance",
            description="Manages financial aspects",
        ),
        Department(
            department_id="D3",
            department_name="Operations",
            description="Oversees operations",
        ),
    ]
    Department.objects.bulk_create(departments)

    print("Inserted Department data...")

    # Insert data into Contact Department
    ContactDepartments = [
        ContactDepartment(
            contact_id=contacts[0],
            department_id=departments[0],
            assignment_date="2024-01-15",
        ),
        ContactDepartment(
            contact_id=contacts[1],
            department_id=departments[1],
            assignment_date="2023-10-05",
        ),
        ContactDepartment(
            contact_id=contacts[2],
            department_id=departments[0],
            assignment_date="2023-07-20",
        ),
    ]
    ContactDepartment.objects.bulk_create(ContactDepartments)

    print("Inserted ContactDepartment data...")

    # Insert data into Role
    roles = [
        Role(
            role_id="R1",
            role_name="Admin",
            description="Administrator with full access to the system",
        ),
        Role(
            role_id="R2",
            role_name="User",
            description="Regular user with limited access",
        ),
    ]
    Role.objects.bulk_create(roles)

    print("Inserted Role data...")

    user_accounts_data = [
        {
            "user_id": "U1",
            "nit": companies[0],
            "username": "john_doe",
            "email": "jdoe@techinnovations.com",
            "password": "default_password",
        },
        {
            "user_id": "U2",
            "nit": companies[1],
            "username": "jane_smith",
            "email": "jsmith@globalfinances.com",
            "password": "default_password",
        },
        {
            "user_id": "U3",
            "nit": companies[2],
            "username": "mary_johnson",
            "email": "mjohnson@healthsolutions.com",
            "password": "default_password",
        },
        {
            "user_id": "U4",
            "nit": companies[3],
            "username": "james_brown",
            "email": "jbrown@ecoenergy.com",
            "password": "default_password",
        },
        {
            "user_id": "U5",
            "nit": companies[4],
            "username": "patricia_garcia",
            "email": "pgarcia@retailgiants.com",
            "password": "default_password",
        },
        {
            "user_id": "U6",
            "nit": companies[5],
            "username": "robert_martinez",
            "email": "rmartinez@autoinnovators.com",
            "password": "default_password",
        },
        {
            "user_id": "U7",
            "nit": companies[6],
            "username": "linda_davis",
            "email": "ldavis@foodiesdelight.com",
            "password": "default_password",
        },
        {
            "user_id": "U8",
            "nit": companies[7],
            "username": "michael_rodriguez",
            "email": "mrodriguez@travelexperts.com",
            "password": "default_password",
        },
        {
            "user_id": "U9",
            "nit": companies[8],
            "username": "barbara_wilson",
            "email": "bwilson@mediamasters.com",
            "password": "default_password",
        },
        {
            "user_id": "U10",
            "nit": companies[9],
            "username": "william_lopez",
            "email": "wlopez@constructionpros.com",
            "password": "default_password",
        },
        {
            "user_id": "U11",
            "nit": companies[10],
            "username": "elizabeth_hernandez",
            "email": "ehernandez@fashionforward.com",
            "password": "default_password",
        },
        {
            "user_id": "U12",
            "nit": companies[11],
            "username": "david_king",
            "email": "dking@techpioneers.com",
            "password": "default_password",
        },
        {
            "user_id": "U13",
            "nit": companies[12],
            "username": "susan_wright",
            "email": "swright@healthfirst.com",
            "password": "default_password",
        },
        {
            "user_id": "U14",
            "nit": companies[13],
            "username": "joseph_green",
            "email": "jgreen@financegurus.com",
            "password": "default_password",
        },
        {
            "user_id": "U15",
            "nit": companies[14],
            "username": "karen_adams",
            "email": "kadams@greenearth.com",
            "password": "default_password",
        },
        {
            "user_id": "U16",
            "nit": companies[15],
            "username": "charles_baker",
            "email": "cbaker@logisticsleaders.com",
            "password": "default_password",
        },
        {
            "user_id": "U17",
            "nit": companies[16],
            "username": "jessica_nelson",
            "email": "jnelson@realestateexperts.com",
            "password": "default_password",
        },
        {
            "user_id": "U18",
            "nit": companies[17],
            "username": "daniel_carter",
            "email": "dcarter@educationinnovators.com",
            "password": "default_password",
        },
        {
            "user_id": "U19",
            "nit": companies[18],
            "username": "nancy_mitchell",
            "email": "nmitchell@entertainmenthub.com",
            "password": "default_password",
        },
        {
            "user_id": "U20",
            "nit": companies[19],
            "username": "paul_perez",
            "email": "pperez@sportsworld.com",
            "password": "default_password",
        },
        {
            "user_id": "U21",
            "nit": companies[20],
            "username": "lisa_roberts",
            "email": "lroberts@beautybliss.com",
            "password": "default_password",
        },
        {
            "user_id": "U22",
            "nit": companies[21],
            "username": "mark_turner",
            "email": "mturner@automotiveexcellence.com",
            "password": "default_password",
        },
        {
            "user_id": "U23",
            "nit": companies[22],
            "username": "sandra_phillips",
            "email": "sphillips@techtitans.com",
            "password": "default_password",
        },
        {
            "user_id": "U24",
            "nit": companies[23],
            "username": "george_campbell",
            "email": "gcampbell@healthcareheroes.com",
            "password": "default_password",
        },
        {
            "user_id": "U25",
            "nit": companies[24],
            "username": "betty_parker",
            "email": "bparker@financewizards.com",
            "password": "default_password",
        },
    ]
    user_accounts = []
    for user_data in user_accounts_data:
        user = UserAccount.objects.create_user(
            username=user_data["username"],
            password=user_data["password"],
            user_id=user_data["user_id"],
            nit=user_data["nit"],
            email=user_data["email"],
        )
        user.save()
        user_accounts.append(user)

    print("Inserted UserAccount data...")

    # Insert data into UserRole
    UserRoles = [
        UserRole(user_id=user_accounts[0], role_id=roles[1]),
        UserRole(user_id=user_accounts[1], role_id=roles[0]),
        UserRole(user_id=user_accounts[2], role_id=roles[1]),
        UserRole(user_id=user_accounts[3], role_id=roles[1]),
        UserRole(user_id=user_accounts[4], role_id=roles[1]),
        UserRole(user_id=user_accounts[5], role_id=roles[1]),
        UserRole(user_id=user_accounts[6], role_id=roles[1]),
        UserRole(user_id=user_accounts[7], role_id=roles[1]),
        UserRole(user_id=user_accounts[8], role_id=roles[1]),
        UserRole(user_id=user_accounts[9], role_id=roles[1]),
        UserRole(user_id=user_accounts[10], role_id=roles[1]),
        UserRole(user_id=user_accounts[11], role_id=roles[1]),
        UserRole(user_id=user_accounts[12], role_id=roles[1]),
        UserRole(user_id=user_accounts[13], role_id=roles[1]),
        UserRole(user_id=user_accounts[14], role_id=roles[1]),
        UserRole(user_id=user_accounts[15], role_id=roles[1]),
        UserRole(user_id=user_accounts[16], role_id=roles[1]),
        UserRole(user_id=user_accounts[17], role_id=roles[1]),
        UserRole(user_id=user_accounts[18], role_id=roles[1]),
        UserRole(user_id=user_accounts[19], role_id=roles[1]),
        UserRole(user_id=user_accounts[20], role_id=roles[1]),
        UserRole(user_id=user_accounts[21], role_id=roles[1]),
        UserRole(user_id=user_accounts[22], role_id=roles[1]),
        UserRole(user_id=user_accounts[23], role_id=roles[1]),
        UserRole(user_id=user_accounts[24], role_id=roles[1]),
    ]
    UserRole.objects.bulk_create(UserRoles)

    print("Inserted UserRole data...")

    # Insert data into Opportunity
    opportunities = [
        Opportunity(
            opportunity_id="O1",
            nit=companies[0],
            contact_id=contacts[0],
            opportunity_name="Cloud Migration Project",
            description="Migrating infrastructure to the cloud",
            estimated_value=50000.00,
            creation_date="2024-05-01",
            estimated_close_date="2024-12-31",
            status="open",
            success_probability=75.0,
        ),
        Opportunity(
            opportunity_id="O2",
            nit=companies[1],
            contact_id=contacts[1],
            opportunity_name="Financial Software Upgrade",
            description="Upgrade finance software for analytics",
            estimated_value=120000.00,
            creation_date="2024-03-15",
            estimated_close_date="2024-11-20",
            status="negotiation",
            success_probability=60.0,
        ),
        Opportunity(
            opportunity_id="O3",
            nit=companies[2],
            contact_id=contacts[2],
            opportunity_name="Healthcare Data Integration",
            description="Integrate data across healthcare units",
            estimated_value=80000.00,
            creation_date="2024-08-01",
            estimated_close_date="2025-01-30",
            status="open",
            success_probability=50.0,
        ),
    ]
    Opportunity.objects.bulk_create(opportunities)

    print("Inserted Opportunity data...")

    # Insert data into Opportunity_Stage
    opportunity_stages = [
        OpportunityStage(
            stage_id="S1",
            stage_name="Qualification",
            description="Identifying the opportunity and qualification",
        ),
        OpportunityStage(
            stage_id="S2",
            stage_name="Proposal",
            description="Proposal of solution to the client",
        ),
        OpportunityStage(
            stage_id="S3",
            stage_name="Negotiation",
            description="Negotiating terms and conditions",
        ),
        OpportunityStage(
            stage_id="S4",
            stage_name="Closure",
            description="Finalizing and closing the deal",
        ),
    ]
    OpportunityStage.objects.bulk_create(opportunity_stages)

    print("Inserted OpportunityStage data...")

    # Insert data into Opportunity_Stage_History
    opportunity_stage_histories = [
        OpportunityStageHistory(
            opportunity_id=opportunities[0],
            stage_id=opportunity_stages[0],
            change_date="2024-05-02",
            notes="Initial qualification with the client",
        ),
        OpportunityStageHistory(
            opportunity_id=opportunities[1],
            stage_id=opportunity_stages[1],
            change_date="2024-06-01",
            notes="Proposal submitted to client for review",
        ),
        OpportunityStageHistory(
            opportunity_id=opportunities[1],
            stage_id=opportunity_stages[2],
            change_date="2024-09-10",
            notes="Negotiation initiated",
        ),
        OpportunityStageHistory(
            opportunity_id=opportunities[2],
            stage_id=opportunity_stages[0],
            change_date="2024-08-05",
            notes="Initial qualification with healthcare provider",
        ),
    ]
    OpportunityStageHistory.objects.bulk_create(opportunity_stage_histories)

    print("Inserted OpportunityStageHistory data...")

    # Insert data into Product_Service
    products_services = [
        ProductService(
            product_service_id="P1",
            product_service_name="Cloud Infrastructure",
            description="Cloud hosting and management services",
            price=1000.00,
        ),
        ProductService(
            product_service_id="P2",
            product_service_name="Financial Analytics Tool",
            description="Software for financial data analysis",
            price=2000.00,
        ),
        ProductService(
            product_service_id="P3",
            product_service_name="Healthcare Data Integration Suite",
            description="Suite for data integration across healthcare units",
            price=1500.00,
        ),
    ]
    ProductService.objects.bulk_create(products_services)

    print("Inserted ProductService data...")

    # Insert data into Opportunity_Product_Service
    opportunity_product_services = [
        OpportunityProductService(
            opportunity_id=opportunities[0],
            product_service_id=products_services[0],
            quantity=50,
            negotiated_price=950.00,
        ),
        OpportunityProductService(
            opportunity_id=opportunities[1],
            product_service_id=products_services[1],
            quantity=60,
            negotiated_price=1800.00,
        ),
        OpportunityProductService(
            opportunity_id=opportunities[2],
            product_service_id=products_services[2],
            quantity=40,
            negotiated_price=1400.00,
        ),
    ]
    OpportunityProductService.objects.bulk_create(opportunity_product_services)

    print("Inserted OpportunityProductService data...")

    # Insert data into Contract
    contracts = [
        Contract(
            contract_id="CT1",
            nit=companies[0],
            contract_number="CNTR-2024-001",
            start_date="2024-01-01",
            end_date="2025-01-01",
            monthly_value=5000.00,
        ),
        Contract(
            contract_id="CT2",
            nit=companies[1],
            contract_number="CNTR-2024-002",
            start_date="2024-06-01",
            end_date="2025-06-01",
            monthly_value=10000.00,
        ),
        Contract(
            contract_id="CT3",
            nit=companies[2],
            contract_number="CNTR-2024-003",
            start_date="2024-03-01",
            end_date="2025-03-01",
            monthly_value=7500.00,
        ),
        Contract(
            contract_id="CT4",
            nit=companies[0],
            contract_number="CNTR-2024-004",
            start_date="2024-04-01",
            end_date="2025-04-01",
            monthly_value=6000.00,
        ),
        Contract(
            contract_id="CT5",
            nit=companies[1],
            contract_number="CNTR-2024-005",
            start_date="2024-08-01",
            end_date="2025-08-01",
            monthly_value=11000.00,
        ),
        Contract(
            contract_id="CT6",
            nit=companies[2],
            contract_number="CNTR-2024-006",
            start_date="2024-09-01",
            end_date="2025-09-01",
            monthly_value=8000.00,
        ),
        Contract(
            contract_id="CT7",
            nit=companies[0],
            contract_number="CNTR-2024-007",
            start_date="2024-10-01",
            end_date="2025-10-01",
            monthly_value=7000.00,
        ),
        Contract(
            contract_id="CT8",
            nit=companies[1],
            contract_number="CNTR-2024-008",
            start_date="2024-12-01",
            end_date="2025-12-01",
            monthly_value=12000.00,
        ),
    ]
    Contract.objects.bulk_create(contracts)

    print("Inserted Contract data...")

    # Insert data into DeliveryCertificate
    delivery_certificates = [
        DeliveryCertificate(
            certificate_id="DC1",
            contract_id=contracts[0],
            delivery_date="2024-01-05",
            notes="Initial delivery for contract CNTR-2024-001",
        ),
        DeliveryCertificate(
            certificate_id="DC2",
            contract_id=contracts[1],
            delivery_date="2024-06-15",
            notes="First delivery for contract CNTR-2024-002",
        ),
        DeliveryCertificate(
            certificate_id="DC3",
            contract_id=contracts[2],
            delivery_date="2024-03-10",
            notes="First delivery for contract CNTR-2024-003",
        ),
        DeliveryCertificate(
            certificate_id="DC4",
            contract_id=contracts[3],
            delivery_date="2024-04-05",
            notes="Delivery for contract CNTR-2024-004",
        ),
        DeliveryCertificate(
            certificate_id="DC5",
            contract_id=contracts[4],
            delivery_date="2024-08-10",
            notes="Initial delivery for contract CNTR-2024-005",
        ),
        DeliveryCertificate(
            certificate_id="DC6",
            contract_id=contracts[5],
            delivery_date="2024-09-15",
            notes="First delivery for contract CNTR-2024-006",
        ),
        DeliveryCertificate(
            certificate_id="DC7",
            contract_id=contracts[6],
            delivery_date="2024-10-15",
            notes="First delivery for contract CNTR-2024-007",
        ),
        DeliveryCertificate(
            certificate_id="DC8",
            contract_id=contracts[7],
            delivery_date="2024-12-05",
            notes="Initial delivery for contract CNTR-2024-008",
        ),
    ]
    DeliveryCertificate.objects.bulk_create(delivery_certificates)

    print("Inserted DeliveryCertificate data...")

    # Insert data into Category
    categories = [
        Category(
            category_id="CAT1",
            category_name="Laptops",
            description="Various brands of laptops",
        ),
        Category(
            category_id="CAT2",
            category_name="Desktops",
            description="Various brands of desktop computers",
        ),
        Category(
            category_id="CAT3",
            category_name="Monitors",
            description="Various brands of monitors",
        ),
    ]
    Category.objects.bulk_create(categories)

    print("Inserted Category data...")

    # Insert data into Equipment
    equipment = [
        Equipment(
            equipment_id="EQ1",
            certificate_id=delivery_certificates[0],
            inventory_code="INV-001",
            description="HP Probook 745",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ2",
            certificate_id=delivery_certificates[0],
            inventory_code="INV-002",
            description="Dell Latitude 5400",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ3",
            certificate_id=delivery_certificates[1],
            inventory_code="INV-003",
            description="Lenovo ThinkPad T480",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ4",
            certificate_id=delivery_certificates[2],
            inventory_code="INV-004",
            description="MacBook Pro 13-inch",
            active=False,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ5",
            certificate_id=delivery_certificates[3],
            inventory_code="INV-005",
            description="Asus ZenBook 14",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ6",
            certificate_id=delivery_certificates[3],
            inventory_code="INV-006",
            description="Acer Aspire 5",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ7",
            certificate_id=delivery_certificates[4],
            inventory_code="INV-007",
            description="Microsoft Surface Pro 7",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ8",
            certificate_id=delivery_certificates[4],
            inventory_code="INV-008",
            description="Razer Blade Stealth 13",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ9",
            certificate_id=delivery_certificates[5],
            inventory_code="INV-009",
            description="HP Envy 13",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ10",
            certificate_id=delivery_certificates[5],
            inventory_code="INV-010",
            description="Lenovo Yoga 730",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ11",
            certificate_id=delivery_certificates[6],
            inventory_code="INV-011",
            description="Dell XPS 13",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ12",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-012",
            description="HP Spectre x360",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ13",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-013",
            description="Toshiba Tecra A50",
            active=True,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ14",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-014",
            description="Apple MacBook Air",
            active=False,
            category_id=categories[0],
        ),
        Equipment(
            equipment_id="EQ15",
            certificate_id=delivery_certificates[0],
            inventory_code="INV-015",
            description="Dell OptiPlex 7070",
            active=True,
            category_id=categories[1],
        ),
        Equipment(
            equipment_id="EQ16",
            certificate_id=delivery_certificates[1],
            inventory_code="INV-016",
            description="HP EliteDesk 800",
            active=True,
            category_id=categories[1],
        ),
        Equipment(
            equipment_id="EQ17",
            certificate_id=delivery_certificates[2],
            inventory_code="INV-017",
            description="Lenovo ThinkCentre M720",
            active=True,
            category_id=categories[1],
        ),
        Equipment(
            equipment_id="EQ18",
            certificate_id=delivery_certificates[3],
            inventory_code="INV-018",
            description="Apple iMac 27-inch",
            active=True,
            category_id=categories[1],
        ),
        Equipment(
            equipment_id="EQ19",
            certificate_id=delivery_certificates[4],
            inventory_code="INV-019",
            description="Samsung 24-inch Monitor",
            active=True,
            category_id=categories[2],
        ),
        Equipment(
            equipment_id="EQ20",
            certificate_id=delivery_certificates[5],
            inventory_code="INV-020",
            description="Dell UltraSharp 27-inch Monitor",
            active=True,
            category_id=categories[2],
        ),
        Equipment(
            equipment_id="EQ21",
            certificate_id=delivery_certificates[6],
            inventory_code="INV-021",
            description="LG 32-inch Monitor",
            active=True,
            category_id=categories[2],
        ),
        Equipment(
            equipment_id="EQ22",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-022",
            description="HP 24-inch Monitor",
            active=True,
            category_id=categories[2],
        ),
    ]
    Equipment.objects.bulk_create(equipment)

    print("Inserted EquipmentData data...")


if __name__ == "__main__":
    reset_database()
    populate_database()
    print("Database has been successfully populated.")
