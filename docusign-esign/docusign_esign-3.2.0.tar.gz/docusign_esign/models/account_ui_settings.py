# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountUISettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, admin_message=None, ask_an_admin=None, enable_admin_message=None, enable_admin_message_metadata=None, enable_easy_sign_can_use_multi_template_apply=None, enable_easy_sign_can_use_multi_template_apply_metadata=None, enable_easy_sign_template_upload=None, enable_easy_sign_template_upload_metadata=None, enable_envelope_copy_with_data=None, enable_envelope_copy_with_data_metadata=None, hide_send_an_envelope=None, hide_send_an_envelope_metadata=None, hide_use_a_template=None, hide_use_a_template_in_prepare=None, hide_use_a_template_in_prepare_metadata=None, hide_use_a_template_metadata=None, order_based_recipient_id_generation=None, order_based_recipient_id_generation_metadata=None, remove_envelope_forwarding=None, remove_envelope_forwarding_metadata=None, should_redact_access_code=None, should_redact_access_code_metadata=None, upload_new_image_to_sign_or_initial=None, upload_new_image_to_sign_or_initial_metadata=None):
        """
        AccountUISettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'admin_message': 'AdminMessage',
            'ask_an_admin': 'AskAnAdmin',
            'enable_admin_message': 'str',
            'enable_admin_message_metadata': 'SettingsMetadata',
            'enable_easy_sign_can_use_multi_template_apply': 'str',
            'enable_easy_sign_can_use_multi_template_apply_metadata': 'SettingsMetadata',
            'enable_easy_sign_template_upload': 'str',
            'enable_easy_sign_template_upload_metadata': 'SettingsMetadata',
            'enable_envelope_copy_with_data': 'str',
            'enable_envelope_copy_with_data_metadata': 'SettingsMetadata',
            'hide_send_an_envelope': 'str',
            'hide_send_an_envelope_metadata': 'SettingsMetadata',
            'hide_use_a_template': 'str',
            'hide_use_a_template_in_prepare': 'str',
            'hide_use_a_template_in_prepare_metadata': 'SettingsMetadata',
            'hide_use_a_template_metadata': 'SettingsMetadata',
            'order_based_recipient_id_generation': 'str',
            'order_based_recipient_id_generation_metadata': 'SettingsMetadata',
            'remove_envelope_forwarding': 'str',
            'remove_envelope_forwarding_metadata': 'SettingsMetadata',
            'should_redact_access_code': 'str',
            'should_redact_access_code_metadata': 'SettingsMetadata',
            'upload_new_image_to_sign_or_initial': 'str',
            'upload_new_image_to_sign_or_initial_metadata': 'SettingsMetadata'
        }

        self.attribute_map = {
            'admin_message': 'adminMessage',
            'ask_an_admin': 'askAnAdmin',
            'enable_admin_message': 'enableAdminMessage',
            'enable_admin_message_metadata': 'enableAdminMessageMetadata',
            'enable_easy_sign_can_use_multi_template_apply': 'enableEasySignCanUseMultiTemplateApply',
            'enable_easy_sign_can_use_multi_template_apply_metadata': 'enableEasySignCanUseMultiTemplateApplyMetadata',
            'enable_easy_sign_template_upload': 'enableEasySignTemplateUpload',
            'enable_easy_sign_template_upload_metadata': 'enableEasySignTemplateUploadMetadata',
            'enable_envelope_copy_with_data': 'enableEnvelopeCopyWithData',
            'enable_envelope_copy_with_data_metadata': 'enableEnvelopeCopyWithDataMetadata',
            'hide_send_an_envelope': 'hideSendAnEnvelope',
            'hide_send_an_envelope_metadata': 'hideSendAnEnvelopeMetadata',
            'hide_use_a_template': 'hideUseATemplate',
            'hide_use_a_template_in_prepare': 'hideUseATemplateInPrepare',
            'hide_use_a_template_in_prepare_metadata': 'hideUseATemplateInPrepareMetadata',
            'hide_use_a_template_metadata': 'hideUseATemplateMetadata',
            'order_based_recipient_id_generation': 'orderBasedRecipientIdGeneration',
            'order_based_recipient_id_generation_metadata': 'orderBasedRecipientIdGenerationMetadata',
            'remove_envelope_forwarding': 'removeEnvelopeForwarding',
            'remove_envelope_forwarding_metadata': 'removeEnvelopeForwardingMetadata',
            'should_redact_access_code': 'shouldRedactAccessCode',
            'should_redact_access_code_metadata': 'shouldRedactAccessCodeMetadata',
            'upload_new_image_to_sign_or_initial': 'uploadNewImageToSignOrInitial',
            'upload_new_image_to_sign_or_initial_metadata': 'uploadNewImageToSignOrInitialMetadata'
        }

        self._admin_message = admin_message
        self._ask_an_admin = ask_an_admin
        self._enable_admin_message = enable_admin_message
        self._enable_admin_message_metadata = enable_admin_message_metadata
        self._enable_easy_sign_can_use_multi_template_apply = enable_easy_sign_can_use_multi_template_apply
        self._enable_easy_sign_can_use_multi_template_apply_metadata = enable_easy_sign_can_use_multi_template_apply_metadata
        self._enable_easy_sign_template_upload = enable_easy_sign_template_upload
        self._enable_easy_sign_template_upload_metadata = enable_easy_sign_template_upload_metadata
        self._enable_envelope_copy_with_data = enable_envelope_copy_with_data
        self._enable_envelope_copy_with_data_metadata = enable_envelope_copy_with_data_metadata
        self._hide_send_an_envelope = hide_send_an_envelope
        self._hide_send_an_envelope_metadata = hide_send_an_envelope_metadata
        self._hide_use_a_template = hide_use_a_template
        self._hide_use_a_template_in_prepare = hide_use_a_template_in_prepare
        self._hide_use_a_template_in_prepare_metadata = hide_use_a_template_in_prepare_metadata
        self._hide_use_a_template_metadata = hide_use_a_template_metadata
        self._order_based_recipient_id_generation = order_based_recipient_id_generation
        self._order_based_recipient_id_generation_metadata = order_based_recipient_id_generation_metadata
        self._remove_envelope_forwarding = remove_envelope_forwarding
        self._remove_envelope_forwarding_metadata = remove_envelope_forwarding_metadata
        self._should_redact_access_code = should_redact_access_code
        self._should_redact_access_code_metadata = should_redact_access_code_metadata
        self._upload_new_image_to_sign_or_initial = upload_new_image_to_sign_or_initial
        self._upload_new_image_to_sign_or_initial_metadata = upload_new_image_to_sign_or_initial_metadata

    @property
    def admin_message(self):
        """
        Gets the admin_message of this AccountUISettings.

        :return: The admin_message of this AccountUISettings.
        :rtype: AdminMessage
        """
        return self._admin_message

    @admin_message.setter
    def admin_message(self, admin_message):
        """
        Sets the admin_message of this AccountUISettings.

        :param admin_message: The admin_message of this AccountUISettings.
        :type: AdminMessage
        """

        self._admin_message = admin_message

    @property
    def ask_an_admin(self):
        """
        Gets the ask_an_admin of this AccountUISettings.

        :return: The ask_an_admin of this AccountUISettings.
        :rtype: AskAnAdmin
        """
        return self._ask_an_admin

    @ask_an_admin.setter
    def ask_an_admin(self, ask_an_admin):
        """
        Sets the ask_an_admin of this AccountUISettings.

        :param ask_an_admin: The ask_an_admin of this AccountUISettings.
        :type: AskAnAdmin
        """

        self._ask_an_admin = ask_an_admin

    @property
    def enable_admin_message(self):
        """
        Gets the enable_admin_message of this AccountUISettings.
        

        :return: The enable_admin_message of this AccountUISettings.
        :rtype: str
        """
        return self._enable_admin_message

    @enable_admin_message.setter
    def enable_admin_message(self, enable_admin_message):
        """
        Sets the enable_admin_message of this AccountUISettings.
        

        :param enable_admin_message: The enable_admin_message of this AccountUISettings.
        :type: str
        """

        self._enable_admin_message = enable_admin_message

    @property
    def enable_admin_message_metadata(self):
        """
        Gets the enable_admin_message_metadata of this AccountUISettings.

        :return: The enable_admin_message_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._enable_admin_message_metadata

    @enable_admin_message_metadata.setter
    def enable_admin_message_metadata(self, enable_admin_message_metadata):
        """
        Sets the enable_admin_message_metadata of this AccountUISettings.

        :param enable_admin_message_metadata: The enable_admin_message_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._enable_admin_message_metadata = enable_admin_message_metadata

    @property
    def enable_easy_sign_can_use_multi_template_apply(self):
        """
        Gets the enable_easy_sign_can_use_multi_template_apply of this AccountUISettings.
        

        :return: The enable_easy_sign_can_use_multi_template_apply of this AccountUISettings.
        :rtype: str
        """
        return self._enable_easy_sign_can_use_multi_template_apply

    @enable_easy_sign_can_use_multi_template_apply.setter
    def enable_easy_sign_can_use_multi_template_apply(self, enable_easy_sign_can_use_multi_template_apply):
        """
        Sets the enable_easy_sign_can_use_multi_template_apply of this AccountUISettings.
        

        :param enable_easy_sign_can_use_multi_template_apply: The enable_easy_sign_can_use_multi_template_apply of this AccountUISettings.
        :type: str
        """

        self._enable_easy_sign_can_use_multi_template_apply = enable_easy_sign_can_use_multi_template_apply

    @property
    def enable_easy_sign_can_use_multi_template_apply_metadata(self):
        """
        Gets the enable_easy_sign_can_use_multi_template_apply_metadata of this AccountUISettings.

        :return: The enable_easy_sign_can_use_multi_template_apply_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._enable_easy_sign_can_use_multi_template_apply_metadata

    @enable_easy_sign_can_use_multi_template_apply_metadata.setter
    def enable_easy_sign_can_use_multi_template_apply_metadata(self, enable_easy_sign_can_use_multi_template_apply_metadata):
        """
        Sets the enable_easy_sign_can_use_multi_template_apply_metadata of this AccountUISettings.

        :param enable_easy_sign_can_use_multi_template_apply_metadata: The enable_easy_sign_can_use_multi_template_apply_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._enable_easy_sign_can_use_multi_template_apply_metadata = enable_easy_sign_can_use_multi_template_apply_metadata

    @property
    def enable_easy_sign_template_upload(self):
        """
        Gets the enable_easy_sign_template_upload of this AccountUISettings.
        

        :return: The enable_easy_sign_template_upload of this AccountUISettings.
        :rtype: str
        """
        return self._enable_easy_sign_template_upload

    @enable_easy_sign_template_upload.setter
    def enable_easy_sign_template_upload(self, enable_easy_sign_template_upload):
        """
        Sets the enable_easy_sign_template_upload of this AccountUISettings.
        

        :param enable_easy_sign_template_upload: The enable_easy_sign_template_upload of this AccountUISettings.
        :type: str
        """

        self._enable_easy_sign_template_upload = enable_easy_sign_template_upload

    @property
    def enable_easy_sign_template_upload_metadata(self):
        """
        Gets the enable_easy_sign_template_upload_metadata of this AccountUISettings.

        :return: The enable_easy_sign_template_upload_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._enable_easy_sign_template_upload_metadata

    @enable_easy_sign_template_upload_metadata.setter
    def enable_easy_sign_template_upload_metadata(self, enable_easy_sign_template_upload_metadata):
        """
        Sets the enable_easy_sign_template_upload_metadata of this AccountUISettings.

        :param enable_easy_sign_template_upload_metadata: The enable_easy_sign_template_upload_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._enable_easy_sign_template_upload_metadata = enable_easy_sign_template_upload_metadata

    @property
    def enable_envelope_copy_with_data(self):
        """
        Gets the enable_envelope_copy_with_data of this AccountUISettings.
        

        :return: The enable_envelope_copy_with_data of this AccountUISettings.
        :rtype: str
        """
        return self._enable_envelope_copy_with_data

    @enable_envelope_copy_with_data.setter
    def enable_envelope_copy_with_data(self, enable_envelope_copy_with_data):
        """
        Sets the enable_envelope_copy_with_data of this AccountUISettings.
        

        :param enable_envelope_copy_with_data: The enable_envelope_copy_with_data of this AccountUISettings.
        :type: str
        """

        self._enable_envelope_copy_with_data = enable_envelope_copy_with_data

    @property
    def enable_envelope_copy_with_data_metadata(self):
        """
        Gets the enable_envelope_copy_with_data_metadata of this AccountUISettings.

        :return: The enable_envelope_copy_with_data_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._enable_envelope_copy_with_data_metadata

    @enable_envelope_copy_with_data_metadata.setter
    def enable_envelope_copy_with_data_metadata(self, enable_envelope_copy_with_data_metadata):
        """
        Sets the enable_envelope_copy_with_data_metadata of this AccountUISettings.

        :param enable_envelope_copy_with_data_metadata: The enable_envelope_copy_with_data_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._enable_envelope_copy_with_data_metadata = enable_envelope_copy_with_data_metadata

    @property
    def hide_send_an_envelope(self):
        """
        Gets the hide_send_an_envelope of this AccountUISettings.
        

        :return: The hide_send_an_envelope of this AccountUISettings.
        :rtype: str
        """
        return self._hide_send_an_envelope

    @hide_send_an_envelope.setter
    def hide_send_an_envelope(self, hide_send_an_envelope):
        """
        Sets the hide_send_an_envelope of this AccountUISettings.
        

        :param hide_send_an_envelope: The hide_send_an_envelope of this AccountUISettings.
        :type: str
        """

        self._hide_send_an_envelope = hide_send_an_envelope

    @property
    def hide_send_an_envelope_metadata(self):
        """
        Gets the hide_send_an_envelope_metadata of this AccountUISettings.

        :return: The hide_send_an_envelope_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._hide_send_an_envelope_metadata

    @hide_send_an_envelope_metadata.setter
    def hide_send_an_envelope_metadata(self, hide_send_an_envelope_metadata):
        """
        Sets the hide_send_an_envelope_metadata of this AccountUISettings.

        :param hide_send_an_envelope_metadata: The hide_send_an_envelope_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._hide_send_an_envelope_metadata = hide_send_an_envelope_metadata

    @property
    def hide_use_a_template(self):
        """
        Gets the hide_use_a_template of this AccountUISettings.
        

        :return: The hide_use_a_template of this AccountUISettings.
        :rtype: str
        """
        return self._hide_use_a_template

    @hide_use_a_template.setter
    def hide_use_a_template(self, hide_use_a_template):
        """
        Sets the hide_use_a_template of this AccountUISettings.
        

        :param hide_use_a_template: The hide_use_a_template of this AccountUISettings.
        :type: str
        """

        self._hide_use_a_template = hide_use_a_template

    @property
    def hide_use_a_template_in_prepare(self):
        """
        Gets the hide_use_a_template_in_prepare of this AccountUISettings.
        

        :return: The hide_use_a_template_in_prepare of this AccountUISettings.
        :rtype: str
        """
        return self._hide_use_a_template_in_prepare

    @hide_use_a_template_in_prepare.setter
    def hide_use_a_template_in_prepare(self, hide_use_a_template_in_prepare):
        """
        Sets the hide_use_a_template_in_prepare of this AccountUISettings.
        

        :param hide_use_a_template_in_prepare: The hide_use_a_template_in_prepare of this AccountUISettings.
        :type: str
        """

        self._hide_use_a_template_in_prepare = hide_use_a_template_in_prepare

    @property
    def hide_use_a_template_in_prepare_metadata(self):
        """
        Gets the hide_use_a_template_in_prepare_metadata of this AccountUISettings.

        :return: The hide_use_a_template_in_prepare_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._hide_use_a_template_in_prepare_metadata

    @hide_use_a_template_in_prepare_metadata.setter
    def hide_use_a_template_in_prepare_metadata(self, hide_use_a_template_in_prepare_metadata):
        """
        Sets the hide_use_a_template_in_prepare_metadata of this AccountUISettings.

        :param hide_use_a_template_in_prepare_metadata: The hide_use_a_template_in_prepare_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._hide_use_a_template_in_prepare_metadata = hide_use_a_template_in_prepare_metadata

    @property
    def hide_use_a_template_metadata(self):
        """
        Gets the hide_use_a_template_metadata of this AccountUISettings.

        :return: The hide_use_a_template_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._hide_use_a_template_metadata

    @hide_use_a_template_metadata.setter
    def hide_use_a_template_metadata(self, hide_use_a_template_metadata):
        """
        Sets the hide_use_a_template_metadata of this AccountUISettings.

        :param hide_use_a_template_metadata: The hide_use_a_template_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._hide_use_a_template_metadata = hide_use_a_template_metadata

    @property
    def order_based_recipient_id_generation(self):
        """
        Gets the order_based_recipient_id_generation of this AccountUISettings.
        

        :return: The order_based_recipient_id_generation of this AccountUISettings.
        :rtype: str
        """
        return self._order_based_recipient_id_generation

    @order_based_recipient_id_generation.setter
    def order_based_recipient_id_generation(self, order_based_recipient_id_generation):
        """
        Sets the order_based_recipient_id_generation of this AccountUISettings.
        

        :param order_based_recipient_id_generation: The order_based_recipient_id_generation of this AccountUISettings.
        :type: str
        """

        self._order_based_recipient_id_generation = order_based_recipient_id_generation

    @property
    def order_based_recipient_id_generation_metadata(self):
        """
        Gets the order_based_recipient_id_generation_metadata of this AccountUISettings.

        :return: The order_based_recipient_id_generation_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._order_based_recipient_id_generation_metadata

    @order_based_recipient_id_generation_metadata.setter
    def order_based_recipient_id_generation_metadata(self, order_based_recipient_id_generation_metadata):
        """
        Sets the order_based_recipient_id_generation_metadata of this AccountUISettings.

        :param order_based_recipient_id_generation_metadata: The order_based_recipient_id_generation_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._order_based_recipient_id_generation_metadata = order_based_recipient_id_generation_metadata

    @property
    def remove_envelope_forwarding(self):
        """
        Gets the remove_envelope_forwarding of this AccountUISettings.
        

        :return: The remove_envelope_forwarding of this AccountUISettings.
        :rtype: str
        """
        return self._remove_envelope_forwarding

    @remove_envelope_forwarding.setter
    def remove_envelope_forwarding(self, remove_envelope_forwarding):
        """
        Sets the remove_envelope_forwarding of this AccountUISettings.
        

        :param remove_envelope_forwarding: The remove_envelope_forwarding of this AccountUISettings.
        :type: str
        """

        self._remove_envelope_forwarding = remove_envelope_forwarding

    @property
    def remove_envelope_forwarding_metadata(self):
        """
        Gets the remove_envelope_forwarding_metadata of this AccountUISettings.

        :return: The remove_envelope_forwarding_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._remove_envelope_forwarding_metadata

    @remove_envelope_forwarding_metadata.setter
    def remove_envelope_forwarding_metadata(self, remove_envelope_forwarding_metadata):
        """
        Sets the remove_envelope_forwarding_metadata of this AccountUISettings.

        :param remove_envelope_forwarding_metadata: The remove_envelope_forwarding_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._remove_envelope_forwarding_metadata = remove_envelope_forwarding_metadata

    @property
    def should_redact_access_code(self):
        """
        Gets the should_redact_access_code of this AccountUISettings.
        

        :return: The should_redact_access_code of this AccountUISettings.
        :rtype: str
        """
        return self._should_redact_access_code

    @should_redact_access_code.setter
    def should_redact_access_code(self, should_redact_access_code):
        """
        Sets the should_redact_access_code of this AccountUISettings.
        

        :param should_redact_access_code: The should_redact_access_code of this AccountUISettings.
        :type: str
        """

        self._should_redact_access_code = should_redact_access_code

    @property
    def should_redact_access_code_metadata(self):
        """
        Gets the should_redact_access_code_metadata of this AccountUISettings.

        :return: The should_redact_access_code_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._should_redact_access_code_metadata

    @should_redact_access_code_metadata.setter
    def should_redact_access_code_metadata(self, should_redact_access_code_metadata):
        """
        Sets the should_redact_access_code_metadata of this AccountUISettings.

        :param should_redact_access_code_metadata: The should_redact_access_code_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._should_redact_access_code_metadata = should_redact_access_code_metadata

    @property
    def upload_new_image_to_sign_or_initial(self):
        """
        Gets the upload_new_image_to_sign_or_initial of this AccountUISettings.
        

        :return: The upload_new_image_to_sign_or_initial of this AccountUISettings.
        :rtype: str
        """
        return self._upload_new_image_to_sign_or_initial

    @upload_new_image_to_sign_or_initial.setter
    def upload_new_image_to_sign_or_initial(self, upload_new_image_to_sign_or_initial):
        """
        Sets the upload_new_image_to_sign_or_initial of this AccountUISettings.
        

        :param upload_new_image_to_sign_or_initial: The upload_new_image_to_sign_or_initial of this AccountUISettings.
        :type: str
        """

        self._upload_new_image_to_sign_or_initial = upload_new_image_to_sign_or_initial

    @property
    def upload_new_image_to_sign_or_initial_metadata(self):
        """
        Gets the upload_new_image_to_sign_or_initial_metadata of this AccountUISettings.

        :return: The upload_new_image_to_sign_or_initial_metadata of this AccountUISettings.
        :rtype: SettingsMetadata
        """
        return self._upload_new_image_to_sign_or_initial_metadata

    @upload_new_image_to_sign_or_initial_metadata.setter
    def upload_new_image_to_sign_or_initial_metadata(self, upload_new_image_to_sign_or_initial_metadata):
        """
        Sets the upload_new_image_to_sign_or_initial_metadata of this AccountUISettings.

        :param upload_new_image_to_sign_or_initial_metadata: The upload_new_image_to_sign_or_initial_metadata of this AccountUISettings.
        :type: SettingsMetadata
        """

        self._upload_new_image_to_sign_or_initial_metadata = upload_new_image_to_sign_or_initial_metadata

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
