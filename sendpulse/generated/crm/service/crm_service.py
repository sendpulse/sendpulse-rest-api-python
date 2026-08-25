from __future__ import annotations

from sendpulse.service.abstract import AbstractService
from sendpulse.generated.crm.service.users_resource import UsersResource
from sendpulse.generated.crm.service.pipelines_resource import PipelinesResource
from sendpulse.generated.crm.service.pipeline_steps_resource import PipelineStepsResource
from sendpulse.generated.crm.service.deals_resource import DealsResource
from sendpulse.generated.crm.service.deal_notes_resource import DealNotesResource
from sendpulse.generated.crm.service.deal_contacts_resource import DealContactsResource
from sendpulse.generated.crm.service.deal_attributes_resource import DealAttributesResource
from sendpulse.generated.crm.service.deal_attribute_value_resource import DealAttributeValueResource
from sendpulse.generated.crm.service.messengers_types_resource import MessengersTypesResource
from sendpulse.generated.crm.service.payments_resource import PaymentsResource
from sendpulse.generated.crm.service.contacts_resource import ContactsResource
from sendpulse.generated.crm.service.contact_phone_number_resource import ContactPhoneNumberResource
from sendpulse.generated.crm.service.contact_email_addresses_resource import ContactEmailAddressesResource
from sendpulse.generated.crm.service.contacts_messengers_resource import ContactsMessengersResource
from sendpulse.generated.crm.service.contact_tags_resource import ContactTagsResource
from sendpulse.generated.crm.service.contact_attributes_resource import ContactAttributesResource
from sendpulse.generated.crm.service.contact_attributes_value_resource import ContactAttributesValueResource
from sendpulse.generated.crm.service.contact_attributes_values_resource import ContactAttributesValuesResource
from sendpulse.generated.crm.service.tasks_boards_resource import TasksBoardsResource
from sendpulse.generated.crm.service.board_attributes_resource import BoardAttributesResource
from sendpulse.generated.crm.service.tasks_steps_resource import TasksStepsResource
from sendpulse.generated.crm.service.tasks_resource import TasksResource
from sendpulse.generated.crm.service.task_comments_resource import TaskCommentsResource
from sendpulse.generated.crm.service.task_tags_resource import TaskTagsResource
from sendpulse.generated.crm.service.task_entity_resource import TaskEntityResource
from sendpulse.generated.crm.service.task_checklist_resource import TaskChecklistResource
from sendpulse.generated.crm.service.checklist_items_resource import ChecklistItemsResource
from sendpulse.generated.crm.service.task_attributes_resource import TaskAttributesResource
from sendpulse.generated.crm.service.telephony_resource import TelephonyResource
from sendpulse.generated.crm.service.deal_expiration_resource import DealExpirationResource
from sendpulse.generated.crm.service.file_manager_resource import FileManagerResource
from sendpulse.generated.crm.service.attachments_resource import AttachmentsResource
from sendpulse.generated.crm.service.company_resource import CompanyResource
from sendpulse.generated.crm.service.company_history_resource import CompanyHistoryResource
from sendpulse.generated.crm.service.company_attributes_resource import CompanyAttributesResource
from sendpulse.generated.crm.service.emails_resource import EmailsResource
from sendpulse.generated.crm.service.phones_resource import PhonesResource
from sendpulse.generated.crm.service.messengers_resource import MessengersResource
from sendpulse.generated.crm.service.deal_history_resource import DealHistoryResource
from sendpulse.generated.crm.service.contact_history_resource import ContactHistoryResource
from sendpulse.generated.crm.service.task_history_resource import TaskHistoryResource
from sendpulse.generated.crm.service.e_commerce_product_resource import ECommerceProductResource
from sendpulse.generated.crm.service.manager_settings_resource import ManagerSettingsResource
from sendpulse.generated.crm.service.custom_tab_resource import CustomTabResource


class CrmService(AbstractService):
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    def pipelines(self) -> PipelinesResource:
        return PipelinesResource(self._client)

    def pipeline_steps(self) -> PipelineStepsResource:
        return PipelineStepsResource(self._client)

    def deals(self) -> DealsResource:
        return DealsResource(self._client)

    def deal_notes(self) -> DealNotesResource:
        return DealNotesResource(self._client)

    def deal_contacts(self) -> DealContactsResource:
        return DealContactsResource(self._client)

    def deal_attributes(self) -> DealAttributesResource:
        return DealAttributesResource(self._client)

    def deal_attribute_value(self) -> DealAttributeValueResource:
        return DealAttributeValueResource(self._client)

    def messengers_types(self) -> MessengersTypesResource:
        return MessengersTypesResource(self._client)

    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    def contact_phone_number(self) -> ContactPhoneNumberResource:
        return ContactPhoneNumberResource(self._client)

    def contact_email_addresses(self) -> ContactEmailAddressesResource:
        return ContactEmailAddressesResource(self._client)

    def contacts_messengers(self) -> ContactsMessengersResource:
        return ContactsMessengersResource(self._client)

    def contact_tags(self) -> ContactTagsResource:
        return ContactTagsResource(self._client)

    def contact_attributes(self) -> ContactAttributesResource:
        return ContactAttributesResource(self._client)

    def contact_attributes_value(self) -> ContactAttributesValueResource:
        return ContactAttributesValueResource(self._client)

    def contact_attributes_values(self) -> ContactAttributesValuesResource:
        return ContactAttributesValuesResource(self._client)

    def tasks_boards(self) -> TasksBoardsResource:
        return TasksBoardsResource(self._client)

    def board_attributes(self) -> BoardAttributesResource:
        return BoardAttributesResource(self._client)

    def tasks_steps(self) -> TasksStepsResource:
        return TasksStepsResource(self._client)

    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    def task_comments(self) -> TaskCommentsResource:
        return TaskCommentsResource(self._client)

    def task_tags(self) -> TaskTagsResource:
        return TaskTagsResource(self._client)

    def task_entity(self) -> TaskEntityResource:
        return TaskEntityResource(self._client)

    def task_checklist(self) -> TaskChecklistResource:
        return TaskChecklistResource(self._client)

    def checklist_items(self) -> ChecklistItemsResource:
        return ChecklistItemsResource(self._client)

    def task_attributes(self) -> TaskAttributesResource:
        return TaskAttributesResource(self._client)

    def telephony(self) -> TelephonyResource:
        return TelephonyResource(self._client)

    def deal_expiration(self) -> DealExpirationResource:
        return DealExpirationResource(self._client)

    def file_manager(self) -> FileManagerResource:
        return FileManagerResource(self._client)

    def attachments(self) -> AttachmentsResource:
        return AttachmentsResource(self._client)

    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    def company_history(self) -> CompanyHistoryResource:
        return CompanyHistoryResource(self._client)

    def company_attributes(self) -> CompanyAttributesResource:
        return CompanyAttributesResource(self._client)

    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    def phones(self) -> PhonesResource:
        return PhonesResource(self._client)

    def messengers(self) -> MessengersResource:
        return MessengersResource(self._client)

    def deal_history(self) -> DealHistoryResource:
        return DealHistoryResource(self._client)

    def contact_history(self) -> ContactHistoryResource:
        return ContactHistoryResource(self._client)

    def task_history(self) -> TaskHistoryResource:
        return TaskHistoryResource(self._client)

    def e_commerce_product(self) -> ECommerceProductResource:
        return ECommerceProductResource(self._client)

    def manager_settings(self) -> ManagerSettingsResource:
        return ManagerSettingsResource(self._client)

    def custom_tab(self) -> CustomTabResource:
        return CustomTabResource(self._client)
