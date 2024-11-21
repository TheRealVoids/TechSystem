import os

import django

# Setting up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techsystem.settings")
django.setup()

from apps.common.services.pgadmin.models import (
    Company,
    Contact,
    ContactDepartment,
    Contract,
    DeliveryCertificate,
    Department,
    Equipment,
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
    ]
    Contact.objects.bulk_create(contacts)

    print("Inserted Contact data...")

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

    # Insert data into UserAccount
    user_accounts = [
        UserAccount(
            user_id="U1",
            nit=companies[0],
            username="john_doe",
            password_hash="hashed_password_example1",
            email="jdoe@techinnovations.com",
        ),
        UserAccount(
            user_id="U2",
            nit=companies[1],
            username="jane_smith",
            password_hash="hashed_password_example2",
            email="jsmith@globalfinances.com",
        ),
        UserAccount(
            user_id="U3",
            nit=companies[2],
            username="mary_johnson",
            password_hash="hashed_password_example3",
            email="mjohnson@healthsolutions.com",
        ),
    ]
    UserAccount.objects.bulk_create(user_accounts)

    print("Inserted UserAccount data...")

    # Insert data into UserRole
    UserRoles = [
        UserRole(user_id=user_accounts[0], role_id=roles[1]),
        UserRole(user_id=user_accounts[1], role_id=roles[0]),
        UserRole(user_id=user_accounts[2], role_id=roles[1]),
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

    # Insert data into Equipment
    equipment = [
        Equipment(
            equipment_id="EQ1",
            certificate_id=delivery_certificates[0],
            inventory_code="INV-001",
            description="HP Probook 745",
            active=True,
        ),
        Equipment(
            equipment_id="EQ2",
            certificate_id=delivery_certificates[0],
            inventory_code="INV-002",
            description="Dell Latitude 5400",
            active=True,
        ),
        Equipment(
            equipment_id="EQ3",
            certificate_id=delivery_certificates[1],
            inventory_code="INV-003",
            description="Lenovo ThinkPad T480",
            active=True,
        ),
        Equipment(
            equipment_id="EQ4",
            certificate_id=delivery_certificates[2],
            inventory_code="INV-004",
            description="MacBook Pro 13-inch",
            active=False,
        ),
        Equipment(
            equipment_id="EQ5",
            certificate_id=delivery_certificates[3],
            inventory_code="INV-005",
            description="Asus ZenBook 14",
            active=True,
        ),
        Equipment(
            equipment_id="EQ6",
            certificate_id=delivery_certificates[3],
            inventory_code="INV-006",
            description="Acer Aspire 5",
            active=True,
        ),
        Equipment(
            equipment_id="EQ7",
            certificate_id=delivery_certificates[4],
            inventory_code="INV-007",
            description="Microsoft Surface Pro 7",
            active=True,
        ),
        Equipment(
            equipment_id="EQ8",
            certificate_id=delivery_certificates[4],
            inventory_code="INV-008",
            description="Razer Blade Stealth 13",
            active=True,
        ),
        Equipment(
            equipment_id="EQ9",
            certificate_id=delivery_certificates[5],
            inventory_code="INV-009",
            description="HP Envy 13",
            active=True,
        ),
        Equipment(
            equipment_id="EQ10",
            certificate_id=delivery_certificates[5],
            inventory_code="INV-010",
            description="Lenovo Yoga 730",
            active=True,
        ),
        Equipment(
            equipment_id="EQ11",
            certificate_id=delivery_certificates[6],
            inventory_code="INV-011",
            description="Dell XPS 13",
            active=True,
        ),
        Equipment(
            equipment_id="EQ12",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-012",
            description="HP Spectre x360",
            active=True,
        ),
        Equipment(
            equipment_id="EQ13",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-013",
            description="Toshiba Tecra A50",
            active=True,
        ),
        Equipment(
            equipment_id="EQ14",
            certificate_id=delivery_certificates[7],
            inventory_code="INV-014",
            description="Apple MacBook Air",
            active=False,
        ),
    ]
    Equipment.objects.bulk_create(equipment)

    print("Inserted EquipmentData data...")


if __name__ == "__main__":
    reset_database()
    populate_database()
    print("Database has been successfully populated.")
