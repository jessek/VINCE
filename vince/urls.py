#########################################################################
# VINCE
#
# Copyright 2023 Carnegie Mellon University.
#
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING
# INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON
# UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
# AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR
# PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE
# MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND
# WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#
# Released under a MIT (SEI)-style license, please see license.txt or contact
# permission@sei.cmu.edu for full terms.
#
# [DISTRIBUTION STATEMENT A] This material has been approved for public
# release and unlimited distribution.  Please see Copyright notice for non-US
# Government use and distribution.
#
# Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
# U.S. Patent and Trademark Office by Carnegie Mellon University.
#
# This Software includes and/or makes use of Third-Party Software each subject
# to its own license.
#
# DM21-1126
########################################################################
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from vince import views
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from cogauth import views as cogauth_views
from vinny.views import userapproverequest

# DO NOT USE "vuls" or "comm" in the URL Path... these are special keywords in the
# database router that change the request variable to use a different database

urlpatterns = [
    re_path('^$', RedirectView.as_view(pattern_name="vince:dashboard"), name='index'),
    re_path('misconfigured/', views.ErrorView.as_view(), name='misconfigured'),
    re_path(r'^attachments/(?P<path>.*)$', views.AttachmentView.as_view(), name='attachment'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/team/', views.TeamDashView.as_view(), name='teamdash'),
    re_path(r'^dashboard/team/(?P<pk>[0-9]+)/$', views.TeamDashView.as_view(), name='teamdash'),
    path('dashboard/stats/', views.DashboardStatsView.as_view(), name='dstat'),
    path('dashboard/posts/', views.DashboardPostView.as_view(), name='dpost'),
    path('dashboard/posts/activity/', views.DashboardPostActivityView.as_view(), name='dpostactivity'),
    path('dashboard/case/activity/', views.DashboardCaseChartView.as_view(), name='dashcase'),
    path('preferences/', views.PreferenceView.as_view(), name='preferences'),
    path('reminders/', views.RemindersView.as_view(), name='reminders'),
    path('reminders/new/', views.NewReminderView.as_view(), name='newreminder'),
    path('reminders/remove/', views.RemoveReminderView.as_view(), name='rmreminder'),
    path('teams/', views.VinceTeamsView.as_view(), name='teams'),
    path('teams/settings/', views.VinceTeamSettingsView.as_view(), name='teamsettings'),
    re_path(r'^teams/settings/(?P<pk>[0-9]+)/$', views.VinceTeamSettingsView.as_view(), name='teamsettings'),
    path('user/admin/', views.VinceUserAdminView.as_view(), name='useradmin'),
    path('user/admin/contacts/reports/', views.VinceContactReportsView.as_view(), name='contactreports'),
    re_path(r'^user/admin/contacts/reports/(?P<type>[1-5])/$', views.VinceContactReportsView.as_view(), name='contactreports'),
    path('roles/', views.TriageRoleView.as_view(), name='roles'),
    path('tags/', views.VinceTagManagerView.as_view(), name='tags'),
    re_path(r'^tags/team/(?P<pk>[0-9]+)/$', views.VinceTagManagerView.as_view(), name='tags'),
    re_path(r'^tags/new/(?P<pk>[0-9]+)/(?P<group>[0-9]+)?/?$', views.VinceNewTagView.as_view(), name='newtag'),
    path('newticket/', views.CreateTicketView.as_view(), name='newticket'),
    re_path(r'^newticket/team/(?P<pk>[0-9]+)/$', views.CreateTicketView.as_view(), name='newteamticket'),
    path('create/user/', views.CreateNewVinceUserView.as_view(), name='create_user'),
    re_path(r'^newticket/(?P<case_id>[0-9]+)/$', views.CreateTicketView.as_view(), name='newticket'),
    path('newcr/', views.CreateNewCaseRequestView.as_view(), name='newcr'),
    re_path(r'^newcr/team/(?P<pk>[0-9]+)/$', views.CreateNewCaseRequestView.as_view(), name='newteamcr'),
    path('addvendor/', views.AddVendorToCase.as_view(), name='addvendor'),
    path('upload/', views.UploadFile.as_view(), name='upload'),
    re_path(r'file/unattach/(?P<pk>[0-9]+)/$', views.UnattachVinceFile.as_view(), name='unattachfile'),
    re_path(r'^casevendor/edit/date/(?P<pk>[0-9]+)/$', views.ChangeVendorNotifyDate.as_view(), name='editvendordate'),
    re_path(r'^casevendor/confirm/edit/date/(?P<pk>[0-9]+)/$', views.ConfirmVendorNotifyDate.as_view(), name='confirmvendordate'),
    path('addparticipant/', views.AddParticipantToCase.as_view(), name='addparticipant'),
    re_path(r'^participant/(?P<pk>[0-9]+)/$', views.ChangeParticipantType.as_view(), name='partype'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/$', views.CaseVendors.as_view(), name='casevendors'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/(?P<notify>notify)/$', views.NotifyVendorsListView.as_view(), name='casevendornotify'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/status/$', views.VendorStatusView.as_view(), name='vendorstatus'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/status/changes/$', views.VendorStatusChangesView.as_view(), name='vendorstmtchanges'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/status/edit/$', views.EditVendorStatusView.as_view(), name='editvendorstatus'),
    re_path(r'^casevendor/(?P<vendor_id>[0-9]+)/status/edit/(?P<pk>[0-9]+)/$', views.VendorVulStatement.as_view(), name='getvulstmt'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/modal/status/$', views.VendorStatusModalView.as_view(), name='vendorstatusmodal'),
    re_path(r'^casevendor/(?P<pk>[0-9]+)/viewed/$', views.VendorViewDetailView.as_view(), name='vendorviewed'),
    re_path(r'^vul/(?P<pk>[0-9]+)/approve/$', views.ApproveVendorStmt.as_view(), name='approvestmt'),
    re_path(r'^vendor/approve/(?P<pk>[0-9]+)/$', views.ApproveVendor.as_view(), name='approve'),
    re_path(r'^participants/(?P<pk>[0-9]+)/$', views.AddParticipantToCase.as_view(), name='caseparticipants'),
    re_path(r'^case/(?P<pk>[0-9]+)/activity/results/$', views.CommunicationsFilterResults.as_view(), name='commfilter'),
    path('ajax_calls/search/', views.autocomplete_vendor),
    path('ajax_calls/calendar/events/', views.calendar_events),
    path('ajax_calls/cwe/', views.autocomplete_cwe),
    path('ajax_calls/user/lookup/', views.vince_user_lookup, name='userlookup'),
    re_path(r'^ajax_calls/references/case/(?P<pk>[0-9]+)/$', views.autocomplete_case_references, name='syncrefs'),
    re_path(r'^ajax_calls/search/(?P<groups>nogroup)/', views.autocomplete_vendor),
    re_path(r'^ajax_calls/contact/(?P<name>.*)/$', views.autocomplete_contact),
    re_path(r'^ajax_calls/pgp/(?P<key_id>.*)/$', views.autocomplete_pgp),
    re_path('ajax_calls/tags/', views.autocomplete_tags, name='auto_tags'),
    path('ajax_calls/casesearch/', views.autocomplete_cases, name='auto_case'),
    re_path(r'^ajax_calls/case/vendors/(?P<pk>[0-9]+)/$', views.autocomplete_casevendors),
    re_path(r'^ajax_calls/case/participants/(?P<pk>[0-9]+)/$', views.autocomplete_caseparticipants),
    re_path(r'^ajax_calls/case/tasks/(?P<pk>[0-9]+)/$', views.autocomplete_casetasks),
    re_path(r'^ajax_calls/case/vulnerabilities/(?P<pk>[0-9]+)/$', views.autocomplete_casevuls),
    path('ticket/results/', views.TicketFilterResults.as_view(), name='ticketresults'),
    re_path(r'^ticket/encrypt/(?P<pk>[0-9]+)/$', views.VinceEncryptandSend.as_view(), name='encrypt'),
    path('ticket/auto/assign/', views.TicketAutoAssign.as_view(), name='autoassign'),
    path('case/results/', views.CaseFilterResults.as_view(), name='caseresults'),
    path('cases/approval/', views.VendorStatusListView.as_view(), name='reqapproval'),
    path('results/', views.AllResults.as_view(), name='results'),
    path('create/contact/', views.CreateContactView.as_view(), name='newcontact'),
    re_path(r'^contact/add/email/(?P<pk>[0-9]+)/$', views.AddEmailToContact.as_view(), name='addemail'),
    path('contact/verify/init/', views.ContactVerifyInit.as_view(), name='initcontactverify'),
    re_path(r'^contact/verify/init/(?P<pk>[0-9]+)/$', views.ContactVerifyInit.as_view(), name='initcontactverify'),
    re_path(r'^contact/admin/lookup/(?P<pk>[0-9]+)/$', views.ContactAdminLookup.as_view(), name='msgadmin'),
    re_path(r'^contact/admin/message/(?P<pk>[0-9]+)/$', views.MessageAdminAddUser.as_view(), name='msgadminadduser'),
    path('contact/verify/list/', views.ContactAssociationListView.as_view(), name='contactlist'),
    path('contact/verify/complete/list/', views.CompletedContactAssociationListView.as_view(), name='complete_contact_list'),
    re_path(r'^contact/verify/request/(?P<pk>[0-9]+)/$', views.ContactRequestAuth.as_view(), name='contactreqauth'),
    re_path(r'^contact/verify/request/complete/(?P<pk>[0-9]+)/$', views.CompleteContactAssociation.as_view(), name='complete_contact'),
    re_path(r'^contact/verify/request/restart/(?P<pk>[0-9]+)/$', views.RestartContactAssociation.as_view(), name='restart_contact'),
    path('generate/', views.generate_vend_id, name="generate"),
    path('create/group/', views.CreateGroupView.as_view(), name='newgroup'),
    re_path(r'^contact/add/group/(?P<pk>[0-9]+)/$', views.AddContactToGroupView.as_view(), name='addtogroup'),
    path('pending/users/', views.ApproveUserView.as_view(), name='pendingusers'),
    path('pending/users/ignored/', views.IgnoredUserView.as_view(), name='ignoredusers'),
    re_path(r'^pending/user/(?P<pk>[0-9]+)/addcontact/$', views.AddUserToContactView.as_view(), name='addusercontact'),
    re_path(r'^pending/users/rm/(?P<pk>[0-9]+)/$', views.RemoveUserCognitoView.as_view(), name='rmuser'),
    re_path(r'^pending/users/(?P<pk>[0-9]+)/$', views.ApproveUserView.as_view(), name='approveuser'),
    path('api/vendors/', views.autocomplete_vendor),
    path('api/users/', views.autocomplete_users),
    path('api/contacts/', views.autocomplete_contacts),
    path('api/users/assignable/', views.autocomplete_assignable_users),
    re_path(r'^api/tickets/team/(?P<pk>[0-9]+)/$', views.autocomplete_team_tickets, name='teamtix'),
    re_path(r'^api/cases/team/(?P<pk>[0-9]+)/$', views.autocomplete_team_cases, name='teamcase'),
    re_path(r'^api/template/(?P<pk>[0-9]+)/$', views.autocomplete_template),
    path('case_management/', views.CaseTemplateMgmtView.as_view(), name='casemgmt'),
    path('email_templates/', views.EmailTemplateMgmtView.as_view(), name='emailtmpls'),
    path('email_template/new/', views.NewEmailTemplate.as_view(), name='newemailtmpl'),
    re_path(r'^email_template/edit/(?P<pk>[0-9]+)/$', views.EditEmailTemplate.as_view(), name='editemailtmpl'),
    re_path(r'^email_template/clone/(?P<pk>[0-9]+)/$', views.CloneEmailTemplate.as_view(), name='cloneemailtmpl'),
    re_path(r'^email_template/delete/(?P<pk>[0-9]+)/$', views.DeleteEmailTemplate.as_view(), name='deleteemailtmpl'),
    path('email_template/filter/', views.EmailTemplateFilterView.as_view(), name='filteremailtmpl'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('reports/users/', views.UserGraphReport.as_view(), name='usergraphs'),
    re_path(r'^reports/(?P<pk>[0-9]+)/$', views.ReportsView.as_view(), name='reports'),
    re_path('reports/print/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.PrintReportsView.as_view(), name='printreport'),
    re_path('reports/(?P<pk>[0-9]+)/print/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.PrintReportsView.as_view(), name='printreport'),
    path('triage/', views.TriageView.as_view(), name='triage'),
    re_path(r'^triage/(?P<pk>[0-9]+)/$', views.TriageView.as_view(), name='triage'),
    path('reports/casesnovendors/', views.CasesWithoutVendorsReport.as_view(), name='cnovreport'),
    re_path(r'^cve/(?P<vul>[0-9]+)/create/$', views.CVEFormView.as_view(), name='newcve'),
    re_path(r'^cve/create/$', views.CVEFormView.as_view(), name='newcve'),
    re_path(r'^cve/(?P<pk>[0-9]+)/download/$', views.DownloadCVEJson, name='download_cve'),
    re_path(r'^cve/(?P<pk>[0-9]+)/cve5/$', views.CreateCVE5Json, name='download_cve5'),
    re_path(r'^cve/(?P<pk>[0-9]+)/cve5/submit/$', views.submitCVE5JSON.as_view(), name='submit_cve5'),        
    re_path(r'^cve/(?P<pk>[0-9]+)/edit/$', views.EditCVEView.as_view(), name='cve'),
    path('case_template/new/', views.NewCaseTemplate.as_view(), name='newtmpl'),
    path('case_template/filter/', views.CaseTemplateFilterView.as_view(), name='filtertmpl'),
    re_path(r'^case_template/delete/(?P<pk>[0-9]+)/$', views.DeleteCaseTemplate.as_view(), name='deletetmpl'),
    re_path(r'^case_template/task/(?P<pk>[0-9]+)/$', views.AddCaseTemplateTask.as_view(), name='casetask'),
    re_path(r'^case_template/task/delete/(?P<pk>[0-9]+)/$', views.DeleteCaseTemplateTask.as_view(), name='deletetask'),
    re_path(r'^case_template/task/clone/(?P<pk>[0-9]+)/$', views.CloneCaseTemplateTask.as_view(), name='clonetask'),
    re_path(r'^case_template/task/edit/(?P<pk>[0-9]+)/$', views.EditCaseTemplateTask.as_view(), name='edittask'),
    re_path(r'^case_template/edit/(?P<pk>[0-9]+)/$', views.EditCaseTemplate.as_view(), name='edittmpl'),
    re_path(r'^case_template/clone/(?P<pk>[0-9]+)/$', views.CloneCaseTemplate.as_view(), name='clonetmpl'),
    re_path(r'^contacts/results/$',views.ContactsResults.as_view(), name='contacts'),
    path('contacts/search/', views.ContactsSearchView.as_view(), name='searchcontacts'),
    path('contacts/updates/', views.ContactUpdateView.as_view(), name='contactupdates'),
    re_path('group/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='group'),
    re_path('group/edit/(?P<pk>[0-9]+)/$', views.GroupEditView.as_view(), name='editgroup'),
    re_path('group/rm/(?P<pk>[0-9]+)/$', views.RemoveGroupView.as_view(), name='rmgroup'),
    re_path('contact/(?P<pk>[0-9]+)/$', views.ContactDetailView.as_view(), name='contact'),
    re_path('contact/rm/(?P<pk>[0-9]+)/$', views.RemoveContactView.as_view(), name='rmcontact'),
    re_path('contact/changes/(?P<pk>[0-9]+)/$', views.ApproveContactInfoChangeView.as_view(), name='contact_changes'),
    re_path('contact/reject/change/(?P<pk>[0-9]+)/$', views.RejectChangeView.as_view(), name='rejectchange'),
    re_path('contact/changes/preview/(?P<pk>[0-9]+)/$', views.ViewAndApproveChangesView.as_view(), name='previewcontact'),
    re_path('contact/vcuser/(?P<pk>[0-9]+)/$', views.VinceCommUserView.as_view(), name='vcuser'),
    re_path('contact/vvuser/(?P<pk>[0-9]+)/$', views.Vince2VCUserView.as_view(), name='vvuser'),
    re_path('contact/vcuser/(?P<pk>[0-9]+)/thread/$', views.VinceCommUserThreadView.as_view(), name='vcuserthread'),
    
    re_path('contact/vcuser/(?P<pk>[0-9]+)/resetmfa/$', views.ResetUserMFAView.as_view(), name='resetusermfa'),
    re_path('contact/vcuser/(?P<pk>[0-9]+)/initiatereset/$', views.InitiateMFAReset.as_view(), name='initiate_reset'),
    re_path('contact/vcuser/(?P<pk>[0-9]+)/rm/$', views.VinceCommRemoveUserView.as_view(), name='vcuser_rm'),
    re_path('contact/edit/(?P<pk>[0-9]+)/$', views.EditContact.as_view(), name='editcontact'),
    re_path('contact/edit/email/modify/(?P<pk>[0-9]+)/$', views.ChangeEmailNotifications.as_view(), name='changeemail'),
    re_path('contact/remove/email/(?P<pk>[0-9]+)/(?P<email>[0-9]+)/$', views.RemoveEmailFromContact.as_view(), name='rmemail'),
    re_path('contact/cases/(?P<pk>[0-9]+)/$', views.ContactCasesView.as_view(), name='contact_cases'),
    re_path('contact/activity/(?P<pk>[0-9]+)/$', views.ContactActivity.as_view(), name='contact_activity'),
    re_path('^search/$', views.SearchAll.as_view(), name='search'),
    re_path('^quickSearch/$', views.quickSearch, name='quicksearch'),
    re_path('^ticket/search/$', views.TicketFilter.as_view(), name='ticketsearch'),
    re_path('^activity/$', views.ActivityView.as_view(), name='activity'),
    path('activity/results/', views.ActivityFilterResults.as_view(), name='activityresults'),
    re_path('^case/search/$', views.CaseFilter.as_view(), name='casesearch'),
    re_path('^case/(?P<pk>[0-9]+)/task/search/$', views.CaseTaskFilter.as_view(), name='casefiltertask'),
    re_path('^removevendor/confirm/(?P<vendor>[0-9]+)/$', views.ConfirmRemoveVendorFromCase.as_view(), name='rmvendorconfirm'),
    re_path('^removeallvendor/confirm/(?P<pk>[0-9]+)/$', views.ConfirmRemoveAllVendorsFromCase.as_view(), name='rmallvendors'),
    re_path('^removevendor/(?P<vendor>[0-9]+)/$', views.RemoveVendorFromCase.as_view(), name='rmvendor'),
    re_path('^editcasevendors/(?P<pk>[0-9]+)/$', views.EditVendorCaseList.as_view(), name='editvendorlist'),
    re_path('^rmpart/(?P<cp>[0-9]+)/$', views.RemoveParticipantFromCase.as_view(), name='rmpartnoconfirm'),
    re_path('^removeparticipant/(?P<cp>[0-9]+)/$', views.ConfirmRemoveParticipant.as_view(), name='rmparticipant'),
    re_path('^taguser/(?P<case_id>[0-9]+)/$', views.TagUser.as_view(), name='taguser'),
    re_path('^newcr/(?P<ticket_id>[0-9]+)/$', views.CreateNewCaseRequestView.as_view(), name='newcr'),
    re_path('^newcr/case/(?P<case_id>[0-9]+)/$', views.CreateNewCaseRequestView.as_view(), name='newcrcase'),
    re_path('^vrf/(?P<pk>[0-9]+)/$', views.CRVRFFullScreen.as_view(), name='vrffullscreen'),
    re_path('^newcase/(?P<ticket_id>[0-9]+)/$', views.CreateNewCaseView.as_view(), name='newcase'),
    re_path('^ticket/(?P<pk>[0-9]+)/activity/$', views.TicketActivityView.as_view(), name='ticket_activity'),
    re_path('^ticket/(?P<pk>[0-9]+)/assign/team/$', views.AssignTicketNewTeam.as_view(), name='assignteam'),
    re_path('^ticket/(?P<pk>[0-9]+)/artifact/$', views.AddTicketArtifactView.as_view(), name='artifact'),
    re_path('^case/(?P<pk>[0-9]+)/artifact/$', views.AddCaseArtifactView.as_view(), name='case_artifact'),
    re_path('^ticket/(?P<pk>[0-9]+)/artifact/(?P<artifact>[0-9]+)/$', views.RemoveTicketArtifact.as_view(), name='rmartifact'),
    re_path('^case/artifact/delete/(?P<pk>[0-9]+)/$', views.RemoveCaseArtifact.as_view(), name='rmcase_artifact'),
    re_path('^ticket/(?P<pk>[0-9]+)/artifact/edit/$', views.AddTicketArtifactView.as_view(), name='editartifacts'),
    re_path('^case/(?P<pk>[0-9]+)/artifact/edit/$', views.AddCaseArtifactView.as_view(), name='editcase_artifacts'),
    re_path('artifact/(?P<pk>[0-9]+)/edit/$', views.EditArtifactView.as_view(), name='editartifact'),
    re_path('^ticket/(?P<pk>[0-9]+)/$', views.TicketView.as_view(), name='ticket'),
    re_path('^case/(?P<pk>[0-9]+)/activity/$', views.CaseActivityView.as_view(), name='case_activity'),
    re_path('^case/(?P<pk>[0-9]+)/$', views.CaseView.as_view(), name='case'),
    re_path('^case/(?P<pk>[0-9]+)/tickets/$', views.CaseTicketView.as_view(), name='casetickets'),
    re_path('^case/(?P<pk>[0-9]+)/transfer/$', views.RequestCaseTransferView.as_view(), name='reqtransfer'),
    re_path('^case/(?P<pk>[0-9]+)/transfer/complete/$', views.CompleteCaseTransferView.as_view(), name='transfer'),
    re_path('^case/(?P<pk>[0-9]+)/transfer/reject/$', views.RejectCaseTransferView.as_view(), name='reject_transfer'),
    re_path('^tickets/dashboard/(?P<type>(Open|Progress|Message))?/$', views.DashboardTicketView.as_view(), name='dashboardtickets'),
    re_path('^dash/case/(?P<pk>[0-9]+)/activity/$', views.DashboardCaseActivityView.as_view(), name='dashactivity'),
    re_path('^dash/queue/(?P<title>(Open|Progress|Message))/activity/$', views.DashboardQueueActivityView.as_view(), name='dashqueue'),
    re_path('^case/(?P<pk>[0-9]+)?/mute/$', views.MuteCaseView.as_view(), name='mutecase'),
    re_path('^case/(?P<pk>[0-9]+)/edit/$', views.EditCaseView.as_view(), name='editcase'),
    re_path('^case/(?P<pk>[0-9]+)/update/$', views.UpdateCaseView.as_view(), name='updatecase'),
    re_path('^case/(?P<pk>[0-9]+)/update/confirm/$', views.ConfirmCaseUpdateStatus.as_view(), name='updateconfirm'),
    re_path('^case/(?P<pk>[0-9]+)/notify/$', views.WritePost.as_view(), name='notify'),
    re_path('^case/(?P<pk>[0-9]+)/notify/crview/$', views.WritePostCRView.as_view(), name='post_crview'),
    re_path('^case/(?P<pk>[0-9]+)/notify/(?P<notify_id>[0-9]+)/$', views.WritePost.as_view(), name='editnotify'),
    re_path('^case/(?P<pk>[0-9]+)/notify/crview/(?P<notify_id>[0-9]+)/$', views.WritePostCRView.as_view(), name='editpost_crview'),
    re_path('^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(), name="post"),
    re_path('^notify/(?P<pk>[0-9]+)/$', views.NotifyParticipant.as_view(), name='notify_participant'),
    re_path('^case/(?P<pk>[0-9]+)/approve/$', views.ApproveAllStatements.as_view(), name='approveall'),
    re_path('^case/(?P<pk>[0-9]+)/send/$', views.NotifyVendor.as_view(), name='sendnotification'),
    re_path('^case/(?P<pk>[0-9]+)/notify/draft/$', views.NotifyVendorFormView.as_view(), name='vnotifydraft'),
    re_path('^case/notify/(?P<pk>[0-9]+)/$', views.NotificationView.as_view(), name='notification'),
    re_path('^case/notify/(?P<pk>[0-9]+)/push/$', views.PushNotification.as_view(), name='push_notify'),
    re_path('^case/notify/(?P<pk>[0-9]+)/remove/$', views.DeletePostView.as_view(), name='delete_post'),
    re_path('^case/(?P<pk>[0-9]+)/artifact/share/$', views.MakeArtifactPublic.as_view(), name='makepublic'),
    re_path('^case/(?P<pk>[0-9]+)/ticket/artifact/share/$', views.MakeTicketArtifactPublic.as_view(), name='maketktpublic'),
    re_path('^case/(?P<case>[0-9]+)/artifacts/$', views.CaseArtifacts.as_view(), name='caseartifacts'),
    re_path('^cr/(?P<pk>[0-9]+)/$', views.CaseRequestView.as_view(), name='cr'),
    re_path('^add_dependency/(?P<ticket_id>[0-9]+)/$', views.AddTicketDependency.as_view(), name='adddep'),
    re_path('^rm_dependency/(?P<ticket_id>[0-9]+)/(?P<dep_id>[0-9]+)/$', views.DeleteTicketDependency.as_view(), name='rmdep'),
    re_path('^add_case_dependency/(?P<case_id>[0-9]+)/$', views.AddCaseDependency.as_view(), name='addcasedep'),
    re_path('^rm_case_dependency/(?P<case_id>[0-9]+)/(?P<dep_id>[0-9]+)/$', views.DeleteCaseDependency.as_view(), name='rmcasedep'),
    re_path('^ticket_cc/(?P<pk>[0-9]+)/$', views.TicketView.as_view(), name='ticket_cc'),
    re_path('^delete/(?P<ticket_id>[0-9]+)/$', views.DeleteTicketView.as_view(), name='delete'),
    re_path('^edit/(?P<ticket_id>[0-9]+)/$', views.EditTicketView.as_view(), name='edit'),
    re_path('^edit/resolution/(?P<pk>[0-9]+)/$', views.EditTicketResolutionView.as_view(), name='editres'),
    re_path('^editcr/(?P<ticket_id>[0-9]+)/$', views.EditCaseRequestView.as_view(), name='editcr'),
    re_path('^ticket/(?P<ticket_id>[0-9]+)/update/$', views.UpdateTicketView.as_view(), name='update'),
    #re_path('^case/(?P<case_id>[0-9]+)/update/$', views.UpdateTicketView.as_view(), name='caseupdate'),
    re_path('^ticket/(?P<ticket_id>[0-9]+)/updateclose/$', views.CloseTicketandTagView.as_view(), name='closeticket'),
    re_path('^hold/(?P<ticket_id>[0-9]+)/$', views.hold_ticket, name='hold'),
    re_path('^unhold/(?P<ticket_id>[0-9]+)/$', views.unhold_ticket, name='unhold'),
    re_path('^followup_edit/(?P<pk>[0-9]+)/$', views.FollowupEditView.as_view(), name='followup_edit'),
#    re_path('^followup_delete/(?P<ticket_id>[0-9]+)/(?P<followup_id>[0-9]+)/$', views.followup_delete, name='followup_delete'),
    re_path('^tickets/(?P<ticket_id>[0-9]+)/attachment_delete/(?P<attachment_id>[0-9]+)/$', views.DeleteAttachment.as_view(), name='attachment_del'),
    re_path('^create/(?P<case_id>[0-9]+)/$', views.CreateVulNote.as_view(), name='create'),
    re_path('^vulnote/(?P<pk>[0-9]+)/$', views.EditVulNote.as_view(), name='edit_vulnote'),
    re_path('^vulnote/download/(?P<pk>[0-9]+)/$', views.DownloadVulNote.as_view(), name='download_vulnote'),
    re_path('^artifact/detail/(?P<pk>[0-9]+)/$', views.ArtifactDetailView.as_view(), name='artifact_detail'),
    re_path('^artifact/share/(?P<pk>[0-9]+)/$', views.ShareArtifactView.as_view(), name='artifact_share'),
    re_path('^artifact/(?P<post>post)/share/(?P<pk>[0-9]+)/$', views.ShareArtifactView.as_view(), name='post_artifact_share'),
    re_path('^vulnote/diff/(?P<revision_id>[0-9]+)/$', views.VulNoteDiffView.as_view(), name='diff'),
    re_path('^vulnote/preview/(?P<pk>[0-9]+)/(?P<revision_id>[0-9]+)/$', views.VulNoteRevisionPreview.as_view(), name='preview'),
    re_path('^vulnote/change_revision/(?P<pk>[0-9]+)/(?P<revision_id>[0-9]+)/$', views.VulNoteChangeRevision.as_view(), name='change_revision'),
    re_path('^vulnote/(?P<pk>[0-9]+)/approve/$', views.ApproveVulNote.as_view(), name='approvevulnote'),
    re_path('^vulnote/(?P<pk>[0-9]+)/review/$', views.VulNoteReviewal.as_view(), name='vulnotereviewal'),
    re_path('^vulnote/(?P<pk>[0-9]+)/review/ask/$', views.AskApprovalVulNote.as_view(), name='askapproval'),
    re_path('^vulnote/(?P<pk>[0-9]+)/review/view/$', views.VulNoteReviewView.as_view(), name='review'),
    re_path('^vulnote/(?P<pk>[0-9]+)/review/detail/$', views.VulNoteReviewDetail.as_view(), name='reviewdetail'),
    re_path('^vulnote/(?P<pk>[0-9]+)/review/apply/$', views.ApplyVulNoteReview.as_view(), name='reviewapply'),
    re_path('^vulnote/(?P<pk>[0-9]+)/publish/$', views.PublishVulNote.as_view(), name='publish'),
    re_path('^vulnote/(?P<pk>[0-9]+)/share/$', views.ShareVulNote.as_view(), name='sharevulnote'),
    re_path('^vulnote/changelog/(?P<pk>[0-9]+)/$', views.VulNoteChangeLog.as_view(), name='changelog'),
    re_path('^case/(?P<pk>[0-9]+)/addvul/$', views.AddVul.as_view(), name='addvul'),
    re_path('^case/(?P<pk>[0-9]+)/editvulns/$', views.EditVulList.as_view(), name='editvuls'),
    re_path('^case/editvul/(?P<pk>[0-9]+)/$', views.EditVul.as_view(), name='editvul'),
    re_path('^case/vuln/ssvc/(?P<pk>[0-9]+)/$', views.VulSSVCView.as_view(), name='vulssvc'),
    re_path('^case/vuln/rm/ssvc/(?P<pk>[0-9]+)/$', views.RemoveVulSSVCView.as_view(), name='rmvulssvc'),
    re_path('^case/vuln/cvss/(?P<pk>[0-9]+)/$', views.VulCVSSView.as_view(), name='vulcvss'),
    re_path('^case/vuln/rm/cvss/(?P<pk>[0-9]+)/$', views.RemoveVulCVSSView.as_view(), name='rmvulcvss'),
    re_path('^case/exploit/edit/(?P<pk>[0-9]+)/$', views.EditExploitView.as_view(), name='editexploit'),
    re_path('^case/exploit/add/(?P<pk>[0-9]+)/$', views.AddExploitView.as_view(), name='addexploit'),
    re_path('^case/exploit/rm/(?P<pk>[0-9]+)/$', views.RemoveExploitView.as_view(), name='rmexploit'),
    re_path('^case/clonevul/(?P<pk>[0-9]+)/$', views.CloneVulnerability.as_view(), name='clonevul'),
    re_path('^case/(?P<case_id>[0-9]+)/rmvul/(?P<pk>[0-9]+)/$', views.RemoveVulnerability.as_view(), name='rmvul'),
    re_path('^case/vul/detail/(?P<pk>[0-9]+)/$', views.VulnerabilityDetailView.as_view(), name='vul_detail'),
    re_path('^case/exploit/share/(?P<pk>[0-9]+)/$', views.ShareExploitView.as_view(), name='shareexploit'),
    re_path('^vul/(?P<pk>[0-9]+)/$', views.VulnerabilityView.as_view(), name='vul'),
    re_path('^vul/reserve/cve/(?P<pk>[0-9]+)/$', views.VulReserveCVEView.as_view(), name='reservecve'),
    path('vul/reserve/cve/', views.VulReserveCVEView.as_view(), name='reservecve'),
    path('email/create/', views.CreateNewEmailView.as_view(), name='newemail'),
    re_path('^email/reply/(?P<reply>[0-9]+)/$', views.CreateNewEmailView.as_view(), name='replyemail'),
    re_path('^email/create/(?P<pk>[0-9]+)/$', views.CreateNewEmailView.as_view(), name='newemail'),
    re_path('^email/create/admins/(?P<admins>admins)/(?P<pk>[0-9]+)/$', views.CreateNewEmailView.as_view(), name='newemailadmins'),
    re_path('^email/create/(?P<user>user)/(?P<pk>[0-9]+)/$', views.CreateNewEmailView.as_view(), name='newemailuser'),
    re_path('^email/create/tkt/(?P<tkt>[0-9]+)/$', views.CreateNewEmailView.as_view(), name='newemailtkt'),

    re_path('^email/create/all/$', views.SendEmailAll.as_view(), name='emailall'),
    path('email/', views.EmailFilterView.as_view(), name='email'),
    path('email/results/', views.EmailFilterResults.as_view(), name='emailresults'),
    path('email/process/', views.ReadEmailAdminView.as_view(), name='process_email'),
    path('user/report/', views.UserReportView.as_view(), name='user_report'),
    path('user/remote/search/', views.CognitoSearchUser.as_view(), name='cognito_change_user'),
    path('user/remote/detail/', views.CognitoGetUserDetails.as_view(), name='cognito_user'),
    path('user/remote/edit/', views.CognitoChangeUserAttributes.as_view(), name='cognito_edit_user'),
    path('triage/addevent/', views.TriageAddEvent.as_view(), name='triage_add'),
    path('triage/removeevent/', views.TriageRemoveEvent.as_view(), name='triage_remove'),
    path('manage/autoassignment/', views.ManageAutoAssignmentView.as_view(), name='manage_auto_assign'),
    path('manage/cve/', views.CVEServicesDashboard.as_view(), name='cve_dashboard'),
    re_path(r'^manage/cve/(?P<pk>[0-9]+)/$', views.CVEServicesDashboard.as_view(), name='cve_dashboard'),
    path('manage/cve/add/', views.CVEServicesManageAccount.as_view(), name='cve_manage'),
    re_path('^manage/cve/edit/(?P<pk>[0-9]+)/', views.CVEServicesManageAccount.as_view(), name='cve_manage'),
    re_path('^manage/role/adduser/(?P<pk>[0-9]+)/$', views.ManageRoleAddUser.as_view(), name='adduserrole'),
    re_path('^manage/cve/detail/(?P<pk>[0-9]+)/', views.CVEServicesDetailAccount.as_view(), name='cve_detail'),
    re_path('^manage/cve/detail/single/(?P<pk>[0-9]+)/(?P<cveid>CVE-\d+-\d+)/', views.CVESingleDetailView.as_view(), name='detailedcve'),
    re_path('^manage/cve/(?P<pk>[0-9]+)/list/', views.CVEListReserved.as_view(), name='cvelist'),
    re_path('^manage/cve/(?P<pk>[0-9]+)/key/', views.CVEAccountViewKey.as_view(), name='cveviewkey'),
    re_path('^manage/cve/delete/(?P<pk>[0-9]+)/', views.CVEServicesDeleteAccount.as_view(), name='cve_services_delete'),
    path('manage/bounces/', views.VINCEBounceManager.as_view(), name='bouncemanager'),
    #Cross applications app url views from vinny.views
    path('api/userapprove/', userapproverequest, {"caller": "vince"}, name='userapprove'),
]
try:
    if (settings.MULTIURL_CONFIG or settings.VINCE_NAMESPACE == "vince") and not settings.LOCALSTACK:
        urlpatterns.extend([
            path('login/', cogauth_views.COGLoginView.as_view(template_name='vince/tracklogin.html'), name="login"),
            path('login/mfa/', cogauth_views.MFAAuthRequiredView.as_view(), name='mfaauth'),
            path('logout/', auth_views.LogoutView.as_view(template_name='vince/tracklogout.html'), name="logout"),

        ])
    else:
        urlpatterns.extend([
            path('login/', auth_views.LoginView.as_view(extra_context={'token_login':1}, template_name='vince/login.html'), name='login'),
            path('logout/', auth_views.LogoutView.as_view(template_name='vince/logout.html'), name="logout"),
        ])
        

except:
    urlpatterns.extend([
        path('login/', auth_views.LoginView.as_view(template_name='vince/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='vince/logout.html'), name="logout")
    ])

if settings.DEBUG:
    urlpatterns.extend([
        path('tokens/', views.VinnyTokens.as_view(), name='tokens'),
        path('token/login/', views.TokenLogin.as_view(), name='vince_token_login'),
    ])
        
