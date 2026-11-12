# GENERATED IDE/type-checker stubs — not imported at runtime. Do not edit by hand.
# Regenerate with generate_stubs.py. 793 operations.
from __future__ import annotations

from typing import Any

class _A360Autoresponders:
    def autorespondersConversions(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersConversionsGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/group-stat-filtered

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/group-stat-filtered

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersIndex(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersList(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/list
        """
        ...

    def autorespondersTotalStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/total-stats

        Params:
          id: int [path] (required)
          flow_type: string [query]
          deleted: string [query]
        """
        ...

class _A360AutorespondersConversions:
    def autorespondersConversionsAll(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/all

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersConversionsGoal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/goal/{goalId}

        Params:
          id: int [path] (required)
          goalId: int [path] (required)
        """
        ...

    def autorespondersConversionsGoals(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/goal

        Params:
          id: int [path] (required)
        """
        ...

    def autorespondersConversionsMainTrigger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/maintrigger

        Params:
          id: int [path] (required)
        """
        ...

    def conversionsAllGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/all/group-stat-filtered

        Params:
          id: int [path] (required)
        """
        ...

    def conversionsGoalGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/goal/{goalId}/group-stat-filtered

        Params:
          id: int [path] (required)
          goalId: int [path] (required)
        """
        ...

    def conversionsGoalsGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/goals/group-stat-filtered

        Params:
          id: int [path] (required)
        """
        ...

    def conversionsMainTriggerGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/autoresponders/{id}/conversions/list/maintrigger/group-stat-filtered

        Params:
          id: int [path] (required)
        """
        ...

class _A360Events:
    def eventsDeleteLog(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /a360/events/delete-log
        """
        ...

class _A360StatsAction:
    def statsActionGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/action/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsActionGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/action/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsCondition:
    def statsTriggerGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/trigger/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsTriggerGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/trigger/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsEmail:
    def statsEmailAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/email/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsEmailGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/email/{elementId}/group-stat

        Params:
          emails[]: array [query]
          sent_date_from: string [query]
          sent_date_to: string [query]
          elementId: string [path] (required)
        """
        ...

    def statsEmailGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/email/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsFilter:
    def statsFilterGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/filter/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsFilterGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/filter/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsFlowOperator:
    def statsFlowOperatorAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/flow-operator/{elementId}/addresses

        Params:
          sortField: string [query]
          sortDirection: string [query]
          elementId: string [path] (required)
        """
        ...

class _A360StatsGoal:
    def statsGoalGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/goal/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsGoalGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/goal/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsMainTrigger:
    def statsMainTriggerAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/main-trigger/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsMainTriggerGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/main-trigger/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsMainTriggerGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/main-trigger/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsMessenger:
    def statsMessengerAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/messenger/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsMessengerGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/messenger/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsMessengerGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/messenger/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsPause:
    def statsPauseAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/pause/{elementId}/addresses

        Params:
          limit: int [query] (required)
          sortField: string [query]
          elementId: string [path] (required)
        """
        ...

    def statsPauseGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/pause/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsPauseGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/pause/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsPush:
    def statsPushAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/push/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsPushGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/push/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsPushGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/push/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsSMS:
    def statsSmsAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/sms/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsSmsGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/sms/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsSmsGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/sms/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class _A360StatsViber:
    def statsViberAddresses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/viber/{elementId}/addresses

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsViberGroupStat(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/viber/{elementId}/group-stat

        Params:
          elementId: string [path] (required)
        """
        ...

    def statsViberGroupStatFiltered(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /a360/stats/viber/{elementId}/group-stat-filtered

        Params:
          elementId: string [path] (required)
        """
        ...

class A360:
    autoresponders: _A360Autoresponders
    autorespondersConversions: _A360AutorespondersConversions
    events: _A360Events
    statsAction: _A360StatsAction
    statsCondition: _A360StatsCondition
    statsEmail: _A360StatsEmail
    statsFilter: _A360StatsFilter
    statsFlowOperator: _A360StatsFlowOperator
    statsGoal: _A360StatsGoal
    statsMainTrigger: _A360StatsMainTrigger
    statsMessenger: _A360StatsMessenger
    statsPause: _A360StatsPause
    statsPush: _A360StatsPush
    statsSMS: _A360StatsSMS
    statsViber: _A360StatsViber

class _ChatbotAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/account
        """
        ...

class _ChatbotBots:
    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/bots
        """
        ...

class _ChatbotDialogLabels:
    def assignDialogLabels(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /chatbots/dialog-labels/assign
        """
        ...

    def createDialogLabel(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /chatbots/dialog-labels
        """
        ...

    def deleteDialogLabel(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /chatbots/dialog-labels/{dialog_label}

        Params:
          dialog_label: string [path] (required)
        """
        ...

    def getDialogLabels(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/dialog-labels
        """
        ...

    def updateDialogLabel(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /chatbots/dialog-labels/{dialog_label}

        Params:
          dialog_label: string [path] (required)
        """
        ...

class _ChatbotDialogs:
    def filterDialogs(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /chatbots/dialogs
        """
        ...

    def getDialogs(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/dialogs

        Params:
          search_after: string [query]
        """
        ...

class _ChatbotOperatorGroups:
    def addOperatorGroupMembers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /chatbots/operator-groups/{operator_group}/members

        Params:
          operator_group: string [path] (required)
        """
        ...

    def createOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /chatbots/operator-groups
        """
        ...

    def deleteOperatorGroup(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /chatbots/operator-groups/{operator_group}

        Params:
          operator_group: string [path] (required)
        """
        ...

    def deleteOperatorGroupMember(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /chatbots/operator-groups/{operator_group}/members/{operator_group_member}

        Params:
          operator_group: string [path] (required)
          operator_group_member: string [path] (required)
        """
        ...

    def getOperatorGroupMembers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /chatbots/operator-groups/{operator_group}/members

        Params:
          operator_group: string [path] (required)
        """
        ...

    def getOperatorGroups(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/operator-groups
        """
        ...

    def updateOperatorGroup(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /chatbots/operator-groups/{operator_group}

        Params:
          operator_group: string [path] (required)
        """
        ...

class _ChatbotOperators:
    def getOperatorCurrentStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /chatbots/operators/{operator}/statistics/current

        Params:
          operator: int [path] (required)
        """
        ...

    def getOperatorPeriodStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /chatbots/operators/{operator}/statistics/period

        Params:
          operator: int [path] (required)
          from: string [query]
          to: string [query]
        """
        ...

    def getOperators(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /chatbots/operators
        """
        ...

class Chatbot:
    account: _ChatbotAccount
    bots: _ChatbotBots
    dialogLabels: _ChatbotDialogLabels
    dialogs: _ChatbotDialogs
    operatorGroups: _ChatbotOperatorGroups
    operators: _ChatbotOperators

class _CrmAttachments:
    def batchCreateAttachments(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/attachments/batch
        """
        ...

    def createAttachment(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/attachments
        """
        ...

    def deleteAttachment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/attachments/{attachmentId}

        Params:
          attachmentId: string [path] (required)
        """
        ...

    def updateAttachment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/attachments/{attachmentId}

        Params:
          attachmentId: string [path] (required)
        """
        ...

    def uploadFiles(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/files/upload
        """
        ...

class _CrmBoards:
    def createBoard(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/boards
        """
        ...

    def createBoardAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/boards/{boardId}/attributes

        Params:
          boardId: string [path] (required)
        """
        ...

    def createBoardStep(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/boards/{boardId}/steps

        Params:
          boardId: string [path] (required)
        """
        ...

    def getBoard(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/boards/{boardId}

        Params:
          boardId: string [path] (required)
        """
        ...

    def listBoardAttributes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/boards/{boardId}/attributes

        Params:
          boardId: string [path] (required)
        """
        ...

    def listBoards(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/boards
        """
        ...

    def updateBoard(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/boards/{boardId}

        Params:
          boardId: string [path] (required)
        """
        ...

    def updateBoardAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/boards/{boardId}/attributes/{attributeId}

        Params:
          boardId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def updateBoardStep(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/boards/{boardId}/steps/{stepId}

        Params:
          boardId: string [path] (required)
          stepId: string [path] (required)
        """
        ...

class _CrmComments:
    def createCompanyComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/comments

        Params:
          companyId: string [path] (required)
        """
        ...

    def createContactComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/comments

        Params:
          contactId: string [path] (required)
        """
        ...

    def createDealComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/comments

        Params:
          dealId: string [path] (required)
        """
        ...

    def createTaskComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/comments

        Params:
          taskId: string [path] (required)
        """
        ...

    def deleteCompanyComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}/comments/{commentId}

        Params:
          companyId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def deleteContactComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/comments/{commentId}

        Params:
          contactId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def deleteDealComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deals/{dealId}/comments/{commentId}

        Params:
          dealId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def deleteTaskComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/tasks/{taskId}/comments/{commentId}

        Params:
          taskId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def listCompanyComments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/comments

        Params:
          message: string [query]
          limit: int [query]
          offset: int [query]
          companyId: string [path] (required)
        """
        ...

    def listContactComments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/comments

        Params:
          message: string [query]
          limit: int [query]
          offset: int [query]
          contactId: string [path] (required)
        """
        ...

    def listDealComments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/{dealId}/comments

        Params:
          message: string [query]
          limit: int [query]
          offset: int [query]
          dealId: string [path] (required)
        """
        ...

    def listTaskComments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/tasks/{taskId}/comments

        Params:
          message: string [query]
          limit: int [query]
          offset: int [query]
          taskId: string [path] (required)
        """
        ...

    def updateCompanyComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}/comments/{commentId}

        Params:
          companyId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def updateContactComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}/comments/{commentId}

        Params:
          contactId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def updateDealComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/deals/{dealId}/comments/{commentId}

        Params:
          dealId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

    def updateTaskComment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/tasks/{taskId}/comments/{commentId}

        Params:
          taskId: string [path] (required)
          commentId: string [path] (required)
        """
        ...

class _CrmCompanies:
    def batchDeleteCompanies(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/batch-delete
        """
        ...

    def createCompany(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies
        """
        ...

    def deleteCompany(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}

        Params:
          companyId: string [path] (required)
        """
        ...

    def getCompany(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}

        Params:
          companyId: string [path] (required)
        """
        ...

    def getCompanyHistory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/history

        Params:
          dateFrom: string [query]
          dateTo: string [query]
          limit: int [query]
          offset: int [query]
          companyId: string [path] (required)
        """
        ...

    def searchCompanies(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/list
        """
        ...

    def searchCompaniesShort(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/short-data
        """
        ...

    def updateCompany(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}

        Params:
          companyId: string [path] (required)
        """
        ...

class _CrmCompanyAttributes:
    def batchSetCompanyAttributeValues(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/attributes/batch

        Params:
          companyId: string [path] (required)
        """
        ...

    def createCompanyAttribute(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/attributes
        """
        ...

    def deleteCompanyAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/attributes/{attributeId}

        Params:
          attributeId: string [path] (required)
        """
        ...

    def deleteCompanyAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}/attributes/{attributeId}

        Params:
          companyId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def listCompanyAttributeValues(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/attributes

        Params:
          companyId: string [path] (required)
        """
        ...

    def listCompanyAttributes(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/attributes
        """
        ...

    def setCompanyAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/attributes

        Params:
          companyId: string [path] (required)
        """
        ...

    def updateCompanyAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/attributes/{attributeId}

        Params:
          attributeId: string [path] (required)
        """
        ...

    def updateCompanyAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}/attributes/{attributeId}

        Params:
          companyId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

class _CrmCompanyChannels:
    def addCompanyEmail(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/emails

        Params:
          companyId: string [path] (required)
        """
        ...

    def addCompanyMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/messengers

        Params:
          companyId: string [path] (required)
        """
        ...

    def addCompanyPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/phones

        Params:
          companyId: string [path] (required)
        """
        ...

    def batchAddCompanyEmails(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/emails/batch

        Params:
          companyId: string [path] (required)
        """
        ...

    def batchAddCompanyMessengers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/messengers/batch

        Params:
          companyId: string [path] (required)
        """
        ...

    def batchAddCompanyPhones(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/companies/{companyId}/phones/batch

        Params:
          companyId: string [path] (required)
        """
        ...

    def deleteCompanyEmail(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}/emails/{emailId}

        Params:
          companyId: string [path] (required)
          emailId: string [path] (required)
        """
        ...

    def deleteCompanyMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}/messengers/{messengerId}

        Params:
          companyId: string [path] (required)
          messengerId: string [path] (required)
        """
        ...

    def deleteCompanyPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/companies/{companyId}/phones/{phoneId}

        Params:
          companyId: string [path] (required)
          phoneId: string [path] (required)
        """
        ...

    def listCompanyEmails(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/emails

        Params:
          email: string [query]
          limit: int [query]
          offset: int [query]
          companyId: string [path] (required)
        """
        ...

    def listCompanyMessengers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/messengers

        Params:
          companyId: string [path] (required)
        """
        ...

    def listCompanyPhones(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/companies/{companyId}/phones

        Params:
          companyId: string [path] (required)
        """
        ...

    def updateCompanyEmail(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}/emails/{emailId}

        Params:
          companyId: string [path] (required)
          emailId: string [path] (required)
        """
        ...

    def updateCompanyMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}/messengers/{messengerId}

        Params:
          companyId: string [path] (required)
          messengerId: string [path] (required)
        """
        ...

    def updateCompanyPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/companies/{companyId}/phones/{phoneId}

        Params:
          companyId: string [path] (required)
          phoneId: string [path] (required)
        """
        ...

class _CrmContactAttributes:
    def batchSetContactAttributeValues(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/attributes/batch

        Params:
          contactId: string [path] (required)
        """
        ...

    def createContactAttribute(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/attributes
        """
        ...

    def deleteContactAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/attributes/{attributeId}

        Params:
          attributeId: string [path] (required)
        """
        ...

    def deleteContactAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/attributes/{attributeId}

        Params:
          contactId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def listContactAttributeValues(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/attributes

        Params:
          contactId: string [path] (required)
        """
        ...

    def listContactAttributes(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/attributes
        """
        ...

    def setContactAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/attributes

        Params:
          contactId: string [path] (required)
        """
        ...

    def updateContactAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/attributes/{attributeId}

        Params:
          attributeId: string [path] (required)
        """
        ...

    def updateContactAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}/attributes/{attributeId}

        Params:
          contactId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

class _CrmContactChannels:
    def addContactEmails(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/emails

        Params:
          contactId: string [path] (required)
        """
        ...

    def addContactMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/messengers

        Params:
          contactId: string [path] (required)
        """
        ...

    def addContactPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/phones

        Params:
          contactId: string [path] (required)
        """
        ...

    def deleteContactEmail(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/emails/{emailId}

        Params:
          contactId: string [path] (required)
          emailId: string [path] (required)
        """
        ...

    def deleteContactMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/messengers/{messengerId}

        Params:
          contactId: string [path] (required)
          messengerId: string [path] (required)
        """
        ...

    def deleteContactPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/phones/{phoneId}

        Params:
          contactId: string [path] (required)
          phoneId: string [path] (required)
        """
        ...

    def updateContactEmail(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}/emails/{emailId}

        Params:
          contactId: string [path] (required)
          emailId: string [path] (required)
        """
        ...

    def updateContactMessenger(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}/messengers/{messengerId}

        Params:
          contactId: string [path] (required)
          messengerId: string [path] (required)
        """
        ...

    def updateContactPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}/phones/{phoneId}

        Params:
          contactId: string [path] (required)
          phoneId: string [path] (required)
        """
        ...

class _CrmContacts:
    def attachContactToCompany(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/relation/{companyId}

        Params:
          contactId: string [path] (required)
          companyId: string [path] (required)
        """
        ...

    def createContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/create
        """
        ...

    def deleteContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}

        Params:
          contactId: string [path] (required)
        """
        ...

    def detachContactFromCompany(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contacts/{contactId}/relation/{companyId}

        Params:
          contactId: string [path] (required)
          companyId: string [path] (required)
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}

        Params:
          contactId: string [path] (required)
        """
        ...

    def getContactByExternalId(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/external/{externalContactId}

        Params:
          externalContactId: string [path] (required)
        """
        ...

    def getContactByMessengerContactId(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/messenger-external/{messengerContactId}

        Params:
          messengerContactId: string [path] (required)
        """
        ...

    def getContactEduStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/edu-statistic

        Params:
          contactId: string [path] (required)
        """
        ...

    def getContactHistory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/history

        Params:
          fromDate: string [query] (required)
          toDate: string [query] (required)
          contactId: string [path] (required)
        """
        ...

    def listContactDeals(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/deals

        Params:
          contactId: string [path] (required)
        """
        ...

    def listContactEduPayments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contacts/{contactId}/edu-payments

        Params:
          contactId: string [path] (required)
        """
        ...

    def searchContacts(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/get-list
        """
        ...

    def searchContactsByEmail(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/get-list-by-email
        """
        ...

    def updateContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contacts/{contactId}

        Params:
          contactId: string [path] (required)
        """
        ...

class _CrmCustomTabs:
    def addCustomTabAttributes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/custom-tab/{customTabId}/relation

        Params:
          customTabId: string [path] (required)
        """
        ...

    def createCustomTab(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/custom-tab
        """
        ...

    def deleteCustomTab(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/custom-tab/{customTabId}

        Params:
          customTabId: string [path] (required)
        """
        ...

    def listCustomTabs(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/custom-tab
        """
        ...

    def removeCustomTabAttributes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/custom-tab/{customTabId}/relation

        Params:
          customTabId: string [path] (required)
        """
        ...

    def updateCustomTab(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/custom-tab/{customTabId}

        Params:
          customTabId: string [path] (required)
        """
        ...

class _CrmDealAttributes:
    def createDealAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/pipelines/{pipelineId}/attributes

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def deleteDealAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/pipelines/{pipelineId}/attributes/{attributeId}

        Params:
          pipelineId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def deleteDealAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deals/{dealId}/attributes/{attributeId}

        Params:
          dealId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def listDealAttributeValues(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/{dealId}/attributes

        Params:
          dealId: string [path] (required)
        """
        ...

    def listDealAttributes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines/{pipelineId}/attributes

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def listDealAttributesByPipeline(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/attributes/{pipelineId}

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def setDealAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/attributes

        Params:
          dealId: string [path] (required)
        """
        ...

    def updateDealAttribute(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/pipelines/{pipelineId}/attributes/{attributeId}

        Params:
          pipelineId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

    def updateDealAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/deals/{dealId}/attributes/{attributeId}

        Params:
          dealId: string [path] (required)
          attributeId: string [path] (required)
        """
        ...

class _CrmDealContacts:
    def attachContactToDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/contacts/{contactId}

        Params:
          dealId: string [path] (required)
          contactId: string [path] (required)
        """
        ...

    def detachContactFromDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deals/{dealId}/contacts/{contactId}

        Params:
          dealId: string [path] (required)
          contactId: string [path] (required)
        """
        ...

    def listDealContacts(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/{dealId}/contacts

        Params:
          dealId: string [path] (required)
        """
        ...

class _CrmDealExpenses:
    def createDealExpense(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deal-expenses
        """
        ...

    def deleteDealExpense(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deal-expenses/{id}

        Params:
          id: string [path] (required)
        """
        ...

    def getDealExpense(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deal-expenses/{id}

        Params:
          id: string [path] (required)
        """
        ...

    def listDealExpenses(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deal-expenses/deal/{dealId}

        Params:
          dealId: string [path] (required)
        """
        ...

    def updateDealExpense(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/deal-expenses/{id}

        Params:
          id: string [path] (required)
        """
        ...

class _CrmDealProducts:
    def addProductToDeal(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/products/deals
        """
        ...

    def listContactDealProducts(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/products/contacts/{contactId}/deals

        Params:
          contactId: string [path] (required)
        """
        ...

    def listDealProducts(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/products/deals/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def removeProductFromDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/products/categories/{categoryId}/{productId}/deals/{headId}

        Params:
          headId: int [path] (required)
          categoryId: string [path] (required)
          productId: string [path] (required)
        """
        ...

    def updateDealProduct(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/products/deals/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _CrmDeals:
    def changeDealPipeline(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/change-pipeline

        Params:
          dealId: string [path] (required)
        """
        ...

    def createDeal(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals
        """
        ...

    def deleteDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deals/{dealId}

        Params:
          dealId: string [path] (required)
        """
        ...

    def deleteDealExpiration(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/deals/{dealId}/expiration

        Params:
          dealId: string [path] (required)
        """
        ...

    def getDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/{dealId}

        Params:
          dealId: string [path] (required)
        """
        ...

    def getDealHistory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/deals/{dealId}/history

        Params:
          fromDate: string [query] (required)
          toDate: string [query] (required)
          dealId: string [path] (required)
        """
        ...

    def searchDeals(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/get-list
        """
        ...

    def setDealExpiration(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/deals/{dealId}/expiration

        Params:
          dealId: string [path] (required)
        """
        ...

    def updateDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/deals/{dealId}

        Params:
          dealId: string [path] (required)
        """
        ...

class _CrmFailReasons:
    def createFailReason(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/pipelines/{pipelineId}/fail-reasons

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def deleteFailReason(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/pipelines/{pipelineId}/fail-reasons/{reasonId}

        Params:
          pipelineId: string [path] (required)
          reasonId: string [path] (required)
        """
        ...

    def listDealFailReasonEntries(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines/{pipelineId}/deals/{dealId}/fail-reasons

        Params:
          limit: int [query] (required)
          offset: int [query] (required)
          fromDate: string [query] (required)
          toDate: string [query] (required)
          pipelineId: string [path] (required)
          dealId: string [path] (required)
        """
        ...

    def listFailReasons(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines/{pipelineId}/fail-reasons

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def updateFailReason(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/pipelines/{pipelineId}/fail-reasons/{reasonId}

        Params:
          pipelineId: string [path] (required)
          reasonId: string [path] (required)
        """
        ...

class _CrmManagerSettings:
    def createManagerSettings(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/manager-settings
        """
        ...

    def deleteManagerSettings(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/manager-settings/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getManagerSettingsBySection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/manager-settings/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def listManagerSettingSections(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/manager-settings/sections
        """
        ...

    def listManagerSettings(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/manager-settings/managers
        """
        ...

    def updateManagerSettings(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/manager-settings/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _CrmMessengerTypes:
    def listMessengerTypes(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/messenger-types
        """
        ...

class _CrmPayments:
    def approvePayment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/payments/{paymentId}/approve

        Params:
          paymentId: string [path] (required)
        """
        ...

    def cancelPayment(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/payments/{paymentId}/cancel

        Params:
          paymentId: string [path] (required)
        """
        ...

    def createPayment(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/payments
        """
        ...

    def generateContactPaymentLink(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/payments/contact-generate-payment-link
        """
        ...

    def generateDealPaymentLink(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/payments/deal-generate-payment-link
        """
        ...

    def listContactPayments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/payments/contacts/{contactId}

        Params:
          contactId: string [path] (required)
        """
        ...

    def listDealPayments(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/payments/deals/{dealId}

        Params:
          dealId: string [path] (required)
        """
        ...

    def listPaymentMethods(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/payments/user-payment-methods
        """
        ...

    def listPayments(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/payments/all
        """
        ...

class _CrmPipelineSteps:
    def createPipelineStep(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/pipelines/{pipelineId}/steps

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def deletePipelineStep(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/pipelines/{pipelineId}/steps/{stepId}

        Params:
          pipelineId: string [path] (required)
          stepId: string [path] (required)
        """
        ...

    def listPipelineSteps(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines/{pipelineId}/steps

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def updatePipelineStep(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/pipelines/{pipelineId}/steps/{stepId}

        Params:
          pipelineId: string [path] (required)
          stepId: string [path] (required)
        """
        ...

class _CrmPipelines:
    def createPipeline(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/pipelines
        """
        ...

    def getPipeline(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines/{pipelineId}

        Params:
          pipelineId: string [path] (required)
        """
        ...

    def listPipelines(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/pipelines
        """
        ...

    def updatePipeline(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/pipelines/{pipelineId}

        Params:
          pipelineId: string [path] (required)
        """
        ...

class _CrmProductCategories:
    def createProductCategory(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/products/categories
        """
        ...

    def deleteProductCategory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/products/categories/{categoryId}

        Params:
          categoryId: string [path] (required)
        """
        ...

    def listProductCategories(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/products/categories
        """
        ...

    def updateProductCategory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/products/categories/{categoryId}

        Params:
          categoryId: string [path] (required)
        """
        ...

class _CrmProducts:
    def addProductSections(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/products/{productId}/sections

        Params:
          productId: string [path] (required)
        """
        ...

    def createProduct(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/products
        """
        ...

    def deleteProduct(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/products/{productId}

        Params:
          productId: string [path] (required)
        """
        ...

    def deleteProductSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/products/{productId}/sections/{sectionId}

        Params:
          sectionId: int [path] (required)
          productId: string [path] (required)
        """
        ...

    def getProduct(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/products/{productId}

        Params:
          productId: string [path] (required)
        """
        ...

    def searchProducts(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/products/all
        """
        ...

    def updateProduct(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/products/{productId}

        Params:
          productId: string [path] (required)
        """
        ...

    def updateProductPrices(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/products/{productId}/prices

        Params:
          productId: string [path] (required)
        """
        ...

    def updateProductSections(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/products/{productId}/sections

        Params:
          productId: string [path] (required)
        """
        ...

class _CrmTags:
    def attachTagToContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contact-tags/{tagId}/contact/{contactId}

        Params:
          tagId: string [path] (required)
          contactId: string [path] (required)
        """
        ...

    def createContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contact-tags
        """
        ...

    def createTaskTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/task-tags
        """
        ...

    def deleteContactTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contact-tags/{tagId}

        Params:
          tagId: string [path] (required)
        """
        ...

    def deleteTaskTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/task-tags/{tagId}

        Params:
          tagId: string [path] (required)
        """
        ...

    def detachTagFromContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/contact-tags/{tagId}/contact/{contactId}

        Params:
          tagId: string [path] (required)
          contactId: string [path] (required)
        """
        ...

    def detachTagFromTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/task-tags/{tagId}/task/{taskId}

        Params:
          tagId: string [path] (required)
          taskId: string [path] (required)
        """
        ...

    def listContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/contact-tags

        Params:
          name: string [query]
          search: string [query]
        """
        ...

    def listTaskTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/task-tags

        Params:
          name: string [query]
          search: string [query]
        """
        ...

    def updateContactTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/contact-tags/{tagId}

        Params:
          tagId: string [path] (required)
        """
        ...

    def updateTaskTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/task-tags/{tagId}

        Params:
          tagId: string [path] (required)
        """
        ...

class _CrmTaskChecklists:
    def changeChecklistItemOrder(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/checklists/{checklistId}/items/{itemId}

        Params:
          checklistId: string [path] (required)
          itemId: string [path] (required)
        """
        ...

    def createChecklistItem(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/checklists/{checklistId}/items

        Params:
          checklistId: string [path] (required)
        """
        ...

    def createTaskChecklist(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/checklists/single

        Params:
          taskId: string [path] (required)
        """
        ...

    def createTaskChecklists(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/checklists

        Params:
          taskId: string [path] (required)
        """
        ...

    def deleteChecklistItem(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/checklists/{checklistId}/items/{itemId}

        Params:
          checklistId: string [path] (required)
          itemId: string [path] (required)
        """
        ...

    def deleteTaskChecklist(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/tasks/{taskId}/checklists/{checklistId}

        Params:
          taskId: string [path] (required)
          checklistId: string [path] (required)
        """
        ...

    def listTaskChecklists(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/tasks/{taskId}/checklists

        Params:
          taskId: string [path] (required)
        """
        ...

    def updateChecklistItem(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/checklists/{checklistId}/items/{itemId}

        Params:
          checklistId: string [path] (required)
          itemId: string [path] (required)
        """
        ...

    def updateTaskChecklist(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/tasks/{taskId}/checklists/{checklistId}/single

        Params:
          taskId: string [path] (required)
          checklistId: string [path] (required)
        """
        ...

    def updateTaskChecklists(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/tasks/{taskId}/checklists

        Params:
          taskId: string [path] (required)
        """
        ...

class _CrmTasks:
    def attachEntitiesToTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/entity-attach

        Params:
          taskId: string [path] (required)
        """
        ...

    def changeTaskOrder(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/steps/{stepId}/order

        Params:
          taskId: string [path] (required)
          stepId: string [path] (required)
        """
        ...

    def createTask(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks
        """
        ...

    def deleteTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/tasks/{taskId}

        Params:
          taskId: string [path] (required)
        """
        ...

    def deleteTaskAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/{boardId}/attributes/{attributeId}/values/{valueId}

        Params:
          boardId: string [path] (required)
          attributeId: string [path] (required)
          valueId: string [path] (required)
        """
        ...

    def detachContactFromTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/task-contacts/{taskId}/contact/{contactId}

        Params:
          taskId: string [path] (required)
          contactId: string [path] (required)
        """
        ...

    def detachDealFromTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/task-deals/{taskId}/deal/{dealId}

        Params:
          taskId: string [path] (required)
          dealId: string [path] (required)
        """
        ...

    def detachTaskFromTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /crm/v1/task-to-task/{taskHeadId}/task/{taskId}

        Params:
          taskHeadId: int [path] (required)
          taskId: string [path] (required)
        """
        ...

    def getTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/tasks/{taskId}

        Params:
          taskId: string [path] (required)
        """
        ...

    def getTaskHistory(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/tasks/{taskId}/history

        Params:
          fromDate: string [query] (required)
          toDate: string [query] (required)
          taskId: string [path] (required)
        """
        ...

    def searchTasks(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/list
        """
        ...

    def setTaskAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/attributes

        Params:
          taskId: string [path] (required)
        """
        ...

    def setTaskParent(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/tasks/{taskId}/parent

        Params:
          taskId: string [path] (required)
        """
        ...

    def updateTask(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/tasks/{taskId}

        Params:
          taskId: string [path] (required)
        """
        ...

    def updateTaskAttributeValue(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /crm/v1/{boardId}/attributes/{attributeId}/values/{valueId}

        Params:
          boardId: string [path] (required)
          attributeId: string [path] (required)
          valueId: string [path] (required)
        """
        ...

class _CrmTelephony:
    def attachCallToDeal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/attach-call

        Params:
          dealId: string [path] (required)
        """
        ...

    def listCalls(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/telephony/calls/get-list
        """
        ...

    def listContactCalls(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/contacts/{contactId}/get-calls

        Params:
          contactId: string [path] (required)
        """
        ...

    def listDealCalls(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /crm/v1/deals/{dealId}/get-calls

        Params:
          dealId: string [path] (required)
        """
        ...

class _CrmUsers:
    def listUsers(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /crm/v1/users
        """
        ...

class Crm:
    attachments: _CrmAttachments
    boards: _CrmBoards
    comments: _CrmComments
    companies: _CrmCompanies
    companyAttributes: _CrmCompanyAttributes
    companyChannels: _CrmCompanyChannels
    contactAttributes: _CrmContactAttributes
    contactChannels: _CrmContactChannels
    contacts: _CrmContacts
    customTabs: _CrmCustomTabs
    dealAttributes: _CrmDealAttributes
    dealContacts: _CrmDealContacts
    dealExpenses: _CrmDealExpenses
    dealProducts: _CrmDealProducts
    deals: _CrmDeals
    failReasons: _CrmFailReasons
    managerSettings: _CrmManagerSettings
    messengerTypes: _CrmMessengerTypes
    payments: _CrmPayments
    pipelineSteps: _CrmPipelineSteps
    pipelines: _CrmPipelines
    productCategories: _CrmProductCategories
    products: _CrmProducts
    tags: _CrmTags
    taskChecklists: _CrmTaskChecklists
    tasks: _CrmTasks
    telephony: _CrmTelephony
    users: _CrmUsers

class _EduCertificateSections:
    def createCertificateSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/{schoolId}/{courseId}/certificate-section

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def deleteCertificateSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/{schoolId}/{courseId}/certificate-section/{certificateSectionId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          certificateSectionId: int [path] (required)
        """
        ...

    def updateCertificateSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/{schoolId}/{courseId}/certificate-section

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

class _EduCourseTariffs:
    def createCourseTariff(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/tariffs

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def createPaymentMethod(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/payment-method

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def createTariffRenewal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/tariff-renewal

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def deleteCourseTariff(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def deletePaymentMethod(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/payment-method/{paymentId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
          paymentId: int [path] (required)
        """
        ...

    def deleteTariffAdvertisingText(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/advertising-text

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def deleteTariffRenewal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/tariff-renewal/{id}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
          id: int [path] (required)
        """
        ...

    def duplicateCourseTariff(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/duplicate

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def listCourseTariffs(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/courses/{courseId}/tariffs

        Params:
          courseId: int [path] (required)
          ids[]: array [query]
          excludeIds[]: array [query]
          status: int [query]
        """
        ...

    def reorderCourseTariffs(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/order

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def updateCourseTariff(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def updateCourseTariffSettings(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/settings

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def updatePaymentMethod(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/payment-method/{paymentId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
          paymentId: int [path] (required)
        """
        ...

    def updateTariffAccessRestriction(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/access-restriction-settings

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def updateTariffContentAccess(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/accesses/contents/{courseTariffId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def updateTariffFunctionalityAccess(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/accesses/functionality/{courseTariffId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

    def updateTariffRenewal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/tariff-renewal/{id}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
          id: int [path] (required)
        """
        ...

    def updateTariffsEntityAccess(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/accesses/entities

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def upsertTariffAdvertisingText(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/tariffs/{courseTariffId}/advertising-text

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          courseTariffId: int [path] (required)
        """
        ...

class _EduCourses:
    def batchCopyCourseContent(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{courseId}/batch/copy

        Params:
          courseId: int [path] (required)
        """
        ...

    def batchDeleteCourseContent(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{courseId}/batch/delete

        Params:
          courseId: int [path] (required)
        """
        ...

    def batchUpdateCourseContentAccess(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{courseId}/batch/access

        Params:
          courseId: int [path] (required)
        """
        ...

    def createCourse(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses
        """
        ...

    def deleteCourse(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def duplicateCourse(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/duplicate

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def listCourses(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/courses
        """
        ...

    def updateCourse(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

class _EduDomains:
    def checkSubdomainName(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/domains/{name}/{systemDomainId}/check

        Params:
          name: string [path] (required)
          systemDomainId: int [path] (required)
        """
        ...

    def listDomains(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/domains
        """
        ...

    def listSystemDomains(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/domains/available
        """
        ...

class _EduForms:
    def createForm(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/{schoolId}/{courseId}/form

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def deleteForm(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/{schoolId}/{courseId}/form/{formId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          formId: int [path] (required)
        """
        ...

    def saveFormQuestions(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/{schoolId}/{courseId}/form/{formId}/questions

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          formId: int [path] (required)
        """
        ...

    def updateForm(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/{schoolId}/{courseId}/form/{formId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          formId: int [path] (required)
        """
        ...

class _EduHomeworkTasks:
    def createHomework(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/homework/{schoolId}

        Params:
          schoolId: int [path] (required)
        """
        ...

    def deleteHomework(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/homework/{schoolId}/{courseId}/{homeworkId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          homeworkId: int [path] (required)
        """
        ...

    def updateHomework(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/homework/{schoolId}/{homeworkId}

        Params:
          schoolId: int [path] (required)
          homeworkId: int [path] (required)
        """
        ...

class _EduHomeworks:
    def getStudentHomework(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/homeworks/{studentHomeworkId}

        Params:
          studentHomeworkId: int [path] (required)
        """
        ...

    def listHomeworksForChecking(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/homeworks/list/checking

        Params:
          limit: int [query] (required)
          offset: int [query] (required)
          status: string [query]
          courseId: int [query]
          schoolId: int [query]
        """
        ...

    def rateStudentHomework(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/homeworks/{studentHomeworkId}/rate

        Params:
          studentHomeworkId: int [path] (required)
        """
        ...

class _EduLessons:
    def createLesson(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/lesson

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def deleteLesson(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/lesson/{lessonId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          lessonId: int [path] (required)
        """
        ...

    def listCourseLessonsContent(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/courses/{schoolId}/{courseId}/lessons/content

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def listCourseSectionsWithLessons(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/courses/{schoolId}/{courseId}/lessons

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          dateFrom: string [query]
          dateTo: string [query]
          rating: int [query]
          access: string [query]
          module: string [query]
        """
        ...

    def updateLesson(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/lesson/{lessonId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          lessonId: int [path] (required)
        """
        ...

class _EduSchools:
    def createSchool(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/schools
        """
        ...

    def deleteSchool(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/schools/{schoolId}

        Params:
          schoolId: int [path] (required)
        """
        ...

    def listSchools(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/schools
        """
        ...

    def reorderSchools(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/schools/order
        """
        ...

    def updateSchool(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/schools/{schoolId}

        Params:
          schoolId: int [path] (required)
        """
        ...

class _EduSections:
    def createSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/courses/{schoolId}/{courseId}/section

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def deleteSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/courses/{schoolId}/{courseId}/section/{sectionId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          sectionId: int [path] (required)
        """
        ...

    def listSections(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/courses/{schoolId}/{courseId}/section

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def updateSection(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/courses/{schoolId}/{courseId}/section/{sectionId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          sectionId: int [path] (required)
        """
        ...

class _EduStudents:
    def changeStudentCourseProgress(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/{courseId}/change-progress

        Params:
          courseId: int [path] (required)
        """
        ...

    def changeStudentCourseStatus(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/{courseId}/change-status

        Params:
          courseId: int [path] (required)
        """
        ...

    def createStudent(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students
        """
        ...

    def deleteStudent(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/students/{studentId}

        Params:
          studentId: int [path] (required)
        """
        ...

    def getStudentCourseStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/students/course-statistics/{studentId}

        Params:
          studentId: int [path] (required)
        """
        ...

    def markStudentsAsPaid(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/{courseId}/mark-as-paid

        Params:
          courseId: int [path] (required)
        """
        ...

    def removeStudentFromCourse(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/students/{studentId}/{courseId}

        Params:
          studentId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def searchAuditory(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/auditory
        """
        ...

    def searchCourseStudents(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/by-course/{courseId}

        Params:
          courseId: int [path] (required)
        """
        ...

    def updateStudentsAvailabilityDate(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/students/{courseId}/update-availability-date

        Params:
          courseId: int [path] (required)
        """
        ...

class _EduStudentsGroups:
    def listCourseGroups(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/groups/{courseId}

        Params:
          courseId: int [path] (required)
        """
        ...

class _EduTags:
    def listTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /edu/public/v1/tags
        """
        ...

class _EduTests:
    def createTest(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/{schoolId}/{courseId}/tests

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
        """
        ...

    def deleteTest(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /edu/public/v1/{schoolId}/{courseId}/tests/{testId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          testId: int [path] (required)
        """
        ...

    def saveTestQuestions(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /edu/public/v1/{schoolId}/{courseId}/tests/{testId}/questions

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          testId: int [path] (required)
        """
        ...

    def updateTest(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /edu/public/v1/{schoolId}/{courseId}/tests/{testId}

        Params:
          schoolId: int [path] (required)
          courseId: int [path] (required)
          testId: int [path] (required)
        """
        ...

class Edu:
    certificateSections: _EduCertificateSections
    courseTariffs: _EduCourseTariffs
    courses: _EduCourses
    domains: _EduDomains
    forms: _EduForms
    homeworkTasks: _EduHomeworkTasks
    homeworks: _EduHomeworks
    lessons: _EduLessons
    schools: _EduSchools
    sections: _EduSections
    students: _EduStudents
    studentsGroups: _EduStudentsGroups
    tags: _EduTags
    tests: _EduTests

class _EmailBalance:
    def getBalance(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /balance
        """
        ...

    def getBalanceByCurrency(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /balance/{currency}

        Params:
          currency: string [path] (required)
        """
        ...

    def getDetailedBalance(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /user/balance/detail
        """
        ...

class _EmailBlacklist:
    def addToBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /blacklist
        """
        ...

    def getBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /blacklist
        """
        ...

    def removeFromBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /blacklist
        """
        ...

class _EmailCampaigns:
    def cancelCampaign(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /campaigns/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def createCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /campaigns
        """
        ...

    def getCampaignById(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /campaigns/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getCampaignCountryStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /campaigns/{id}/countries

        Params:
          id: int [path] (required)
        """
        ...

    def getCampaignReferralStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /campaigns/{id}/referrals

        Params:
          id: int [path] (required)
        """
        ...

    def getCampaigns(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /campaigns

        Params:
          limit: int [query]
          offset: int [query]
          order: string [query]
          status: array [query]
          planed: bool [query]
        """
        ...

    def getCampaignsByList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/campaigns

        Params:
          id: int [path] (required)
          limit: int [query]
          offset: int [query]
        """
        ...

    def updateCampaign(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PATCH /campaigns/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _EmailEmailAddress:
    def deleteEmailGlobally(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /emails/{email}

        Params:
          email: string [path] (required)
        """
        ...

    def getEmailCampaignInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /campaigns/{id}/email/{email}

        Params:
          id: int [path] (required)
          email: string [path] (required)
        """
        ...

    def getEmailCampaignStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /emails/{email}/campaigns

        Params:
          email: string [path] (required)
        """
        ...

    def getEmailDetails(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /emails/{email}/details

        Params:
          email: string [path] (required)
        """
        ...

    def getEmailFromList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/emails/{email}

        Params:
          id: int [path] (required)
          email: string [path] (required)
        """
        ...

    def getEmailInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /emails/{email}

        Params:
          email: string [path] (required)
        """
        ...

    def getMultipleEmailsCampaignStats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /emails/campaigns
        """
        ...

    def getMultipleEmailsInfo(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /emails
        """
        ...

    def updateContactVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /addressbooks/{id}/emails/variable

        Params:
          id: int [path] (required)
        """
        ...

class _EmailMailingLists:
    def addEmailsToMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /addressbooks/{id}/emails

        Params:
          id: int [path] (required)
        """
        ...

    def createMailingList(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /addressbooks
        """
        ...

    def deleteEmailsFromMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /addressbooks/{id}/emails

        Params:
          id: int [path] (required)
        """
        ...

    def deleteMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /addressbooks/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getCampaignCostByList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/cost

        Params:
          id: int [path] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/variables/{variableName}/{searchValue}

        Params:
          id: int [path] (required)
          variableName: string [path] (required)
          searchValue: string [path] (required)
        """
        ...

    def getEmailsFromMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/emails

        Params:
          id: int [path] (required)
          limit: int [query]
          offset: int [query]
          order: string [query]
          active: bool [query]
          not_active: bool [query]
        """
        ...

    def getEmailsTotalCount(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/emails/total

        Params:
          id: int [path] (required)
          active: bool [query]
        """
        ...

    def getMailingListById(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getMailingListVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /addressbooks/{id}/variables

        Params:
          id: int [path] (required)
        """
        ...

    def getMailingLists(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /addressbooks

        Params:
          limit: int [query]
          offset: int [query]
        """
        ...

    def unsubscribeEmailsFromMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /addressbooks/{id}/emails/unsubscribe

        Params:
          id: int [path] (required)
        """
        ...

    def updateContactPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /addressbooks/{id}/phone

        Params:
          id: int [path] (required)
        """
        ...

    def updateMailingList(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /addressbooks/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _EmailSenders:
    def activateSender(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /senders/{email}/code

        Params:
          email: string [path] (required)
        """
        ...

    def addSender(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /senders
        """
        ...

    def deleteSender(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /senders
        """
        ...

    def getSenders(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /senders
        """
        ...

    def requestSenderActivationCode(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /senders/{email}/code

        Params:
          email: string [path] (required)
        """
        ...

class _EmailTags:
    def createTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tags
        """
        ...

    def deleteTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /tags/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /tags
        """
        ...

    def pinTagToEmail(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tags/pin/email
        """
        ...

    def pinTagToPhone(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tags/pin/phone
        """
        ...

    def unpinTagFromEmail(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tags/unpin/email
        """
        ...

    def unpinTagFromPhone(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tags/unpin/phone
        """
        ...

    def updateTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /tags/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _EmailTemplates:
    def createTemplate(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /template
        """
        ...

    def getTemplateById(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /template/{template_id}

        Params:
          template_id: string [path] (required)
          owner: string [query]
          lang: string [query]
        """
        ...

    def getTemplateBySlug(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /template/slug/{name_slug}

        Params:
          name_slug: string [path] (required)
          owner: string [query]
          lang: string [query]
        """
        ...

    def getTemplates(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /templates

        Params:
          owner: string [query]
          only_active: bool [query]
          limit: int [query]
          offset: int [query]
        """
        ...

    def updateTemplate(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /template/edit/{id}

        Params:
          id: int [path] (required)
        """
        ...

class _EmailWebhooks:
    def createWebhook(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /v2/email-service/webhook
        """
        ...

    def deleteWebhook(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /v2/email-service/webhook/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getWebhookById(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/email-service/webhook/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getWebhooks(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/email-service/webhook
        """
        ...

    def updateWebhook(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /v2/email-service/webhook/{id}

        Params:
          id: int [path] (required)
        """
        ...

class Email:
    balance: _EmailBalance
    blacklist: _EmailBlacklist
    campaigns: _EmailCampaigns
    emailAddress: _EmailEmailAddress
    mailingLists: _EmailMailingLists
    senders: _EmailSenders
    tags: _EmailTags
    templates: _EmailTemplates
    webhooks: _EmailWebhooks

class _FacebookAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /messenger/account
        """
        ...

class _FacebookBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /messenger/bots
        """
        ...

class _FacebookCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/campaigns/send
        """
        ...

class _FacebookChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /messenger/chats

        Params:
          bot_id: string [query]
        """
        ...

class _FacebookContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/closeChat
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /messenger/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /messenger/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/openChat
        """
        ...

    def reactToMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/react
        """
        ...

    def sendMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/send
        """
        ...

    def sendTextMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/sendText
        """
        ...

    def sendTyping(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/sendTyping
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/contacts/updateNote
        """
        ...

class _FacebookFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/flows/runByTrigger
        """
        ...

class _FacebookTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _FacebookTemplates:
    def createTemplate(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /messenger/templates
        """
        ...

    def deleteTemplate(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /messenger/templates/{id}

        Params:
          id: string [path] (required)
          bot_id: string [query] (required)
        """
        ...

    def getTemplates(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/templates

        Params:
          bot_id: string [query] (required)
          name: string [query]
          locale: string [query]
          status: string [query]
        """
        ...

class _FacebookTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _FacebookVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /messenger/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class Facebook:
    account: _FacebookAccount
    bots: _FacebookBots
    campaigns: _FacebookCampaigns
    chats: _FacebookChats
    contacts: _FacebookContacts
    flows: _FacebookFlows
    tags: _FacebookTags
    templates: _FacebookTemplates
    triggers: _FacebookTriggers
    variables: _FacebookVariables

class _FileManagerDirectory:
    def createDirectory(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /fm/public/v1/directory
        """
        ...

    def getDirectoryContents(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /fm/public/v1/directory/{path}

        Params:
          path: string [path] (required)
        """
        ...

    def getDirectoryTree(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /fm/public/v1/directory
        """
        ...

    def getStorageStats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /fm/public/v1/directory/size
        """
        ...

    def searchFiles(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /fm/public/v1/directory/find

        Params:
          search: string [query] (required)
          path: string [query] (required)
        """
        ...

class _FileManagerFile:
    def checkFileExists(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /fm/public/v1/file/exist
        """
        ...

    def deleteFile(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /fm/public/v1/file
        """
        ...

    def filterFiles(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /fm/public/v1/file/filter
        """
        ...

    def uploadFile(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /fm/public/v1/file
        """
        ...

class FileManager:
    directory: _FileManagerDirectory
    file: _FileManagerFile

class _InstagramAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /instagram/account
        """
        ...

class _InstagramBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /instagram/bots
        """
        ...

class _InstagramCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/campaigns/send
        """
        ...

class _InstagramChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /instagram/chats

        Params:
          bot_id: string [query]
        """
        ...

class _InstagramContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/closeChat
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /instagram/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /instagram/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/openChat
        """
        ...

    def reactToMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/react
        """
        ...

    def sendMessages(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/send
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/contacts/updateNote
        """
        ...

class _InstagramFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /instagram/flows/runByTrigger
        """
        ...

class _InstagramTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _InstagramTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _InstagramVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /instagram/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class Instagram:
    account: _InstagramAccount
    bots: _InstagramBots
    campaigns: _InstagramCampaigns
    chats: _InstagramChats
    contacts: _InstagramContacts
    flows: _InstagramFlows
    tags: _InstagramTags
    triggers: _InstagramTriggers
    variables: _InstagramVariables

class _LiveChatAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /live-chat/account
        """
        ...

class _LiveChatBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /live-chat/bots
        """
        ...

class _LiveChatChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /live-chat/chats

        Params:
          bot_id: string [query]
        """
        ...

class _LiveChatContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/closeChat
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /live-chat/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /live-chat/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/openChat
        """
        ...

    def sendMessages(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/send
        """
        ...

    def setContactName(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/setName
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/contacts/updateNote
        """
        ...

class _LiveChatFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /live-chat/flows/runByTrigger
        """
        ...

class _LiveChatTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _LiveChatTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _LiveChatVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /live-chat/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class LiveChat:
    account: _LiveChatAccount
    bots: _LiveChatBots
    chats: _LiveChatChats
    contacts: _LiveChatContacts
    flows: _LiveChatFlows
    tags: _LiveChatTags
    triggers: _LiveChatTriggers
    variables: _LiveChatVariables

class _PopupsPopup:
    def deletePopup(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /v2/pop-ups/popups/{popupId}

        Params:
          popupId: string [path] (required)
        """
        ...

    def listPopupConditions(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/popups/conditions
        """
        ...

    def listPopups(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/popups/list/{projectId}

        Params:
          projectId: string [path] (required)
        """
        ...

    def listQuizPopups(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/popups/list/quiz/{projectId}

        Params:
          projectId: string [path] (required)
        """
        ...

    def setPopupState(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /v2/pop-ups/popups/{popupId}/set-state

        Params:
          popupId: string [path] (required)
        """
        ...

class _PopupsPopupStatistic:
    def getAggregatedNpsStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/statistics/nps/{popupId}/aggregated

        Params:
          popupId: string [path] (required)
        """
        ...

    def getNpsStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/statistics/nps/{popupId}

        Params:
          popupId: string [path] (required)
        """
        ...

    def getPopupStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/statistics/popup/{popupId}

        Params:
          popupId: string [path] (required)
        """
        ...

class _PopupsProject:
    def createProject(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /v2/pop-ups/widgets
        """
        ...

    def listProjects(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/widgets/list
        """
        ...

class _PopupsProjectStatistic:
    def getProjectStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/statistics/widget/{projectId}

        Params:
          projectId: string [path] (required)
        """
        ...

class _PopupsSubscribers:
    def getSubscriber(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/subscribers/get/{subscriberId}

        Params:
          subscriberId: int [path] (required)
        """
        ...

    def listSubscribersByPopup(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/subscribers/by-popup/{popupId}

        Params:
          popupId: string [path] (required)
        """
        ...

    def listSubscribersByProject(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/subscribers/by-project/{projectId}

        Params:
          projectId: string [path] (required)
        """
        ...

class _PopupsTariff:
    def getTariffLimits(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/pop-ups/tariff/limits
        """
        ...

class Popups:
    popup: _PopupsPopup
    popupStatistic: _PopupsPopupStatistic
    project: _PopupsProject
    projectStatistic: _PopupsProjectStatistic
    subscribers: _PopupsSubscribers
    tariff: _PopupsTariff

class _SmsCampaigns:
    def calculateSmsCost(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /sms/campaigns/cost

        Params:
          addressBookId: int [query]
          phones: array [query]
          body: string [query] (required)
          sender: string [query] (required)
          route: mixed [query]
        """
        ...

    def cancelSmsCampaign(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /sms/campaigns/cancel/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def createSmsCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /sms/campaigns
        """
        ...

    def deleteSmsCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /sms/campaigns
        """
        ...

    def getSmsCampaignInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /sms/campaigns/info/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getSmsCampaigns(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /sms/campaigns/list

        Params:
          dateFrom: string [query]
          dateTo: string [query]
        """
        ...

    def sendSmsToNumbers(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /sms/send
        """
        ...

class _SmsCompliance:
    def addSmsBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /sms/black_list
        """
        ...

    def getSmsBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /sms/black_list
        """
        ...

    def removeSmsBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /sms/black_list
        """
        ...

class _SmsConfiguration:
    def getSmsSenders(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /sms/senders
        """
        ...

class _SmsContacts:
    def addSmsNumbers(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /sms/numbers
        """
        ...

    def addSmsNumbersWithVariables(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /sms/numbers/variables
        """
        ...

    def getSmsNumberInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /sms/numbers/info/{addressBookId}/{phoneNumber}

        Params:
          addressBookId: int [path] (required)
          phoneNumber: string [path] (required)
        """
        ...

    def removeSmsNumbers(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /sms/numbers
        """
        ...

    def updateContactPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /addressbooks/{id}/phone

        Params:
          id: int [path] (required)
        """
        ...

    def updateSmsVariablesBatch(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """PUT /sms/numbers
        """
        ...

    def updateSmsVariablesSingle(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /addressbooks/{id}/phones/variable

        Params:
          id: int [path] (required)
        """
        ...

class Sms:
    campaigns: _SmsCampaigns
    compliance: _SmsCompliance
    configuration: _SmsConfiguration
    contacts: _SmsContacts

class _SmtpBounces:
    def getSmtpBouncesDay(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/bounces/day

        Params:
          date: string [query]
          limit: int [query]
          offset: int [query]
        """
        ...

    def getSmtpBouncesTotal(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/bounces/day/total
        """
        ...

class _SmtpConfiguration:
    def addSmtpDomain(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """POST /v2/email-service/smtp/sender_domains/{domain}

        Params:
          domain: string [path] (required)
        """
        ...

    def addSmtpSender(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /senders
        """
        ...

    def getSmtpAllowedDomains(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/email-service/smtp/sender_domains
        """
        ...

    def getSmtpIps(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/ips
        """
        ...

    def getSmtpSenders(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/senders
        """
        ...

class _SmtpEmails:
    def getSmtpEmailInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /smtp/emails/{id}

        Params:
          id: string [path] (required)
        """
        ...

    def getSmtpEmails(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/emails

        Params:
          limit: int [query]
          offset: int [query]
          from: string [query]
          to: string [query]
          sender: string [query]
          recipient: string [query]
          country: string [query]
        """
        ...

    def getSmtpEmailsBatchInfo(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /smtp/emails/info
        """
        ...

    def getSmtpEmailsTotal(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/emails/total
        """
        ...

    def sendSmtpEmail(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /smtp/emails
        """
        ...

class _SmtpUnsubscribe:
    def getSmtpUnsubscribed(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /smtp/unsubscribe

        Params:
          date: string [query]
          limit: int [query]
          offset: int [query]
        """
        ...

    def removeSmtpUnsubscribe(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /smtp/unsubscribe
        """
        ...

    def resubscribeSmtpRecipient(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /smtp/resubscribe
        """
        ...

    def searchSmtpUnsubscribe(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /smtp/unsubscribe/search

        Params:
          email: string [query] (required)
        """
        ...

    def unsubscribeSmtpRecipients(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /smtp/unsubscribe
        """
        ...

class Smtp:
    bounces: _SmtpBounces
    configuration: _SmtpConfiguration
    emails: _SmtpEmails
    unsubscribe: _SmtpUnsubscribe

class _TelegramAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /telegram/account
        """
        ...

class _TelegramBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /telegram/bots
        """
        ...

class _TelegramCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/campaigns/send
        """
        ...

class _TelegramChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /telegram/chats

        Params:
          bot_id: string [query]
        """
        ...

class _TelegramContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/closeChat
        """
        ...

    def createContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactByTelegramId(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/getByTelegramId

        Params:
          bot_id: string [query] (required)
          telegram_id: int [query] (required)
          business_connection_id: string [query]
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /telegram/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /telegram/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/openChat
        """
        ...

    def reactToMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/react
        """
        ...

    def sendMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/send
        """
        ...

    def sendTextMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/sendText
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/contacts/updateNote
        """
        ...

class _TelegramFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /telegram/flows/runByTrigger
        """
        ...

class _TelegramTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _TelegramTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _TelegramVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /telegram/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class Telegram:
    account: _TelegramAccount
    bots: _TelegramBots
    campaigns: _TelegramCampaigns
    chats: _TelegramChats
    contacts: _TelegramContacts
    flows: _TelegramFlows
    tags: _TelegramTags
    triggers: _TelegramTriggers
    variables: _TelegramVariables

class _TiktokAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /tiktok/account
        """
        ...

class _TiktokBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /tiktok/bots
        """
        ...

class _TiktokCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/campaigns/send
        """
        ...

class _TiktokChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /tiktok/chats

        Params:
          bot_id: string [query]
        """
        ...

class _TiktokContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/closeChat
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /tiktok/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /tiktok/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/openChat
        """
        ...

    def sendMessages(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/send
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/contacts/updateNote
        """
        ...

class _TiktokFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /tiktok/flows/runByTrigger
        """
        ...

class _TiktokTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _TiktokTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _TiktokVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /tiktok/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class Tiktok:
    account: _TiktokAccount
    bots: _TiktokBots
    campaigns: _TiktokCampaigns
    chats: _TiktokChats
    contacts: _TiktokContacts
    flows: _TiktokFlows
    tags: _TiktokTags
    triggers: _TiktokTriggers
    variables: _TiktokVariables

class _VerifierMailingListVerification:
    def getVerificationProgress(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/get-progress

        Params:
          id: int [query] (required)
        """
        ...

    def getVerificationResults(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/check

        Params:
          id: int [query] (required)
          start: int [query]
          count: int [query]
        """
        ...

    def getVerifiedLists(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/check-list

        Params:
          start: int [query]
          count: int [query]
        """
        ...

    def verifyMailingList(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /verifier-service/send-list-to-verify
        """
        ...

class _VerifierReports:
    def createVerificationReport(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /verifier-service/make-report
        """
        ...

    def downloadVerificationReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/get-report

        Params:
          id: int [query] (required)
          format: int [query]
        """
        ...

    def viewVerificationReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/check-report

        Params:
          id: int [query] (required)
          format: int [query]
        """
        ...

class _VerifierSingleEmailVerification:
    def getSingleVerificationResult(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /verifier-service/get-single-result

        Params:
          email: string [query] (required)
        """
        ...

    def verifySingleEmail(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /verifier-service/send-single-to-verify
        """
        ...

class Verifier:
    mailingListVerification: _VerifierMailingListVerification
    reports: _VerifierReports
    singleEmailVerification: _VerifierSingleEmailVerification

class _ViberCampaigns:
    def createViberCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber
        """
        ...

    def getViberCampaignStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/task/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getViberCampaigns(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /viber/task

        Params:
          limit: int [query]
          offset: int [query]
        """
        ...

    def getViberRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/task/{id}/recipients

        Params:
          id: int [path] (required)
        """
        ...

class _ViberCompliance:
    def addViberBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /v2/viber-service/phone-exception
        """
        ...

    def getViberBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /v2/viber-service/phone-exception

        Params:
          limit: int [query]
          offset: int [query]
        """
        ...

    def removeViberBlacklist(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """DELETE /v2/viber-service/phone-exception
        """
        ...

class _ViberConfiguration:
    def getViberSenderProfile(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/senders/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getViberSenders(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /viber/senders
        """
        ...

class Viber:
    campaigns: _ViberCampaigns
    compliance: _ViberCompliance
    configuration: _ViberConfiguration

class _ViberChatbotAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/account
        """
        ...

class _ViberChatbotBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/bots
        """
        ...

class _ViberChatbotCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/campaigns/send
        """
        ...

class _ViberChatbotChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/chats

        Params:
          bot_id: string [query]
        """
        ...

class _ViberChatbotContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/closeChat
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /viber/chatbots/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /viber/chatbots/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/openChat
        """
        ...

    def sendMessages(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/send
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/contacts/updateNote
        """
        ...

class _ViberChatbotFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /viber/chatbots/flows/runByTrigger
        """
        ...

class _ViberChatbotTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _ViberChatbotTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _ViberChatbotVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /viber/chatbots/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class ViberChatbot:
    account: _ViberChatbotAccount
    bots: _ViberChatbotBots
    campaigns: _ViberChatbotCampaigns
    chats: _ViberChatbotChats
    contacts: _ViberChatbotContacts
    flows: _ViberChatbotFlows
    tags: _ViberChatbotTags
    triggers: _ViberChatbotTriggers
    variables: _ViberChatbotVariables

class _WebPushCampaigns:
    def createWebPushCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /push/tasks
        """
        ...

    def getWebPushCampaignStats(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/tasks/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getWebPushCampaigns(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /push/tasks

        Params:
          limit: int [query]
          offset: int [query]
          from: string [query]
          to: string [query]
          website_id: int [query]
        """
        ...

class _WebPushConfiguration:
    def getWebPushCode(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/websites/{id}/code

        Params:
          id: int [path] (required)
        """
        ...

class _WebPushSubscribers:
    def getWebPushSubscribersTotal(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/websites/{id}/subscriptions/total

        Params:
          id: int [path] (required)
        """
        ...

    def getWebPushSubscriptions(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/websites/{id}/subscriptions

        Params:
          id: int [path] (required)
          limit: int [query]
          offset: int [query]
          subscription_date_from: string [query]
          subscription_date_to: string [query]
        """
        ...

    def setWebPushSubscriberState(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /push/subscriptions/state
        """
        ...

class _WebPushWebsites:
    def getWebPushVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/websites/{id}/variables

        Params:
          id: int [path] (required)
        """
        ...

    def getWebPushWebsiteInfo(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /push/websites/info/{id}

        Params:
          id: int [path] (required)
        """
        ...

    def getWebPushWebsites(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /push/websites

        Params:
          limit: int [query]
          offset: int [query]
        """
        ...

    def getWebPushWebsitesTotal(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /push/websites/total
        """
        ...

class WebPush:
    campaigns: _WebPushCampaigns
    configuration: _WebPushConfiguration
    subscribers: _WebPushSubscribers
    websites: _WebPushWebsites

class _WhatsappAccount:
    def getAccount(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/account
        """
        ...

class _WhatsappBots:
    def getBotStatistics(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/bots/statistics

        Params:
          bot_id: string [query] (required)
        """
        ...

    def getBots(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/bots
        """
        ...

class _WhatsappCampaigns:
    def getCampaignRecipients(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/campaigns/recipients

        Params:
          id: string [query] (required)
        """
        ...

    def getCampaignReport(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/campaigns/report

        Params:
          id: string [query] (required)
        """
        ...

    def sendCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/campaigns/send
        """
        ...

    def sendTemplateCampaign(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/campaigns/sendTemplate
        """
        ...

class _WhatsappChats:
    def getChatMessages(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/chats/messages

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getChats(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/chats

        Params:
          bot_id: string [query]
        """
        ...

class _WhatsappContacts:
    def assignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/operators/assign
        """
        ...

    def assignContactOperatorGroup(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/operators/assignGroup
        """
        ...

    def closeContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/closeChat
        """
        ...

    def createContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts
        """
        ...

    def createContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/createNote
        """
        ...

    def deleteContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/delete
        """
        ...

    def deleteContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/deleteNote
        """
        ...

    def deleteContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/deletePauseAutomation
        """
        ...

    def deleteContactTag(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/deleteTag
        """
        ...

    def deleteContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/deleteVariable
        """
        ...

    def disableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/disable
        """
        ...

    def enableContact(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/enable
        """
        ...

    def getContact(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/get

        Params:
          id: string [query] (required)
        """
        ...

    def getContactByPhone(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/getByPhone

        Params:
          phone: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactNotes(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/notes

        Params:
          bot_id: string [query] (required)
          contact_id: string [query] (required)
        """
        ...

    def getContactPauseAutomation(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/getPauseAutomation

        Params:
          contact_id: string [query] (required)
        """
        ...

    def getContactsByTag(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/getByTag

        Params:
          tag: string [query] (required)
          bot_id: string [query] (required)
        """
        ...

    def getContactsByVariable(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/contacts/getByVariable

        Params:
          variable_id: string [query]
          variable_name: string [query]
          bot_id: string [query]
          variable_value: string [query] (required)
        """
        ...

    def markContactMessagesRead(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /whatsapp/contacts/mark-read

        Params:
          contact_id: string [query] (required)
        """
        ...

    def markContactMessagesUnread(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """PUT /whatsapp/contacts/mark-unread

        Params:
          contact_id: string [query] (required)
        """
        ...

    def openContactChat(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/openChat
        """
        ...

    def reactToMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/react
        """
        ...

    def sendMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/send
        """
        ...

    def sendMessageByPhone(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/sendByPhone
        """
        ...

    def sendTemplateMessage(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/sendTemplate
        """
        ...

    def sendTemplateMessageByPhone(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/sendTemplateByPhone
        """
        ...

    def sendTyping(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/sendTyping
        """
        ...

    def setContactName(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/setName
        """
        ...

    def setContactPauseAutomation(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/setPauseAutomation
        """
        ...

    def setContactTags(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/setTag
        """
        ...

    def setContactVariable(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/setVariable
        """
        ...

    def unassignContactOperator(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/operators/unAssign
        """
        ...

    def updateContactNote(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/contacts/updateNote
        """
        ...

class _WhatsappFlows:
    def getFlows(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/flows

        Params:
          bot_id: string [query] (required)
        """
        ...

    def runFlow(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/flows/run
        """
        ...

    def runFlowByTrigger(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/flows/runByTrigger
        """
        ...

class _WhatsappTags:
    def getTags(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/tags

        Params:
          bot_id: string [query] (required)
        """
        ...

class _WhatsappTemplates:
    def createTemplate(self, params: dict[str, Any] | None = ...) -> dict[str, Any] | list[Any]:
        """POST /whatsapp/templates
        """
        ...

    def deleteTemplate(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """DELETE /whatsapp/templates/{id}

        Params:
          id: string [path] (required)
          bot_id: string [query] (required)
        """
        ...

    def getTemplates(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/templates

        Params:
          bot_id: string [query] (required)
          name: string [query]
          locale: string [query]
          status: string [query]
          category: string [query]
        """
        ...

class _WhatsappTriggers:
    def getTriggers(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/triggers

        Params:
          bot_id: string [query] (required)
        """
        ...

class _WhatsappVariables:
    def getVariables(self, params: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """GET /whatsapp/variables

        Params:
          bot_id: string [query] (required)
        """
        ...

class Whatsapp:
    account: _WhatsappAccount
    bots: _WhatsappBots
    campaigns: _WhatsappCampaigns
    chats: _WhatsappChats
    contacts: _WhatsappContacts
    flows: _WhatsappFlows
    tags: _WhatsappTags
    templates: _WhatsappTemplates
    triggers: _WhatsappTriggers
    variables: _WhatsappVariables
