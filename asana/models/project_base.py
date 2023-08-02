# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectBase(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gid': 'str',
        'resource_type': 'str',
        'name': 'str',
        'archived': 'bool',
        'color': 'str',
        'created_at': 'datetime',
        'current_status': 'ProjectBaseCurrentStatus',
        'current_status_update': 'ProjectBaseCurrentStatusUpdate',
        'custom_field_settings': 'list[PortfolioResponseCustomFieldSettings]',
        'default_view': 'str',
        'due_date': 'date',
        'due_on': 'date',
        'html_notes': 'str',
        'members': 'list[CustomFieldResponsePeopleValue]',
        'modified_at': 'datetime',
        'notes': 'str',
        'public': 'bool',
        'start_on': 'date'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'archived': 'archived',
        'color': 'color',
        'created_at': 'created_at',
        'current_status': 'current_status',
        'current_status_update': 'current_status_update',
        'custom_field_settings': 'custom_field_settings',
        'default_view': 'default_view',
        'due_date': 'due_date',
        'due_on': 'due_on',
        'html_notes': 'html_notes',
        'members': 'members',
        'modified_at': 'modified_at',
        'notes': 'notes',
        'public': 'public',
        'start_on': 'start_on'
    }

    def __init__(self, gid=None, resource_type=None, name=None, archived=None, color=None, created_at=None, current_status=None, current_status_update=None, custom_field_settings=None, default_view=None, due_date=None, due_on=None, html_notes=None, members=None, modified_at=None, notes=None, public=None, start_on=None):  # noqa: E501
        """ProjectBase - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._archived = None
        self._color = None
        self._created_at = None
        self._current_status = None
        self._current_status_update = None
        self._custom_field_settings = None
        self._default_view = None
        self._due_date = None
        self._due_on = None
        self._html_notes = None
        self._members = None
        self._modified_at = None
        self._notes = None
        self._public = None
        self._start_on = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if archived is not None:
            self.archived = archived
        if color is not None:
            self.color = color
        if created_at is not None:
            self.created_at = created_at
        if current_status is not None:
            self.current_status = current_status
        if current_status_update is not None:
            self.current_status_update = current_status_update
        if custom_field_settings is not None:
            self.custom_field_settings = custom_field_settings
        if default_view is not None:
            self.default_view = default_view
        if due_date is not None:
            self.due_date = due_date
        if due_on is not None:
            self.due_on = due_on
        if html_notes is not None:
            self.html_notes = html_notes
        if members is not None:
            self.members = members
        if modified_at is not None:
            self.modified_at = modified_at
        if notes is not None:
            self.notes = notes
        if public is not None:
            self.public = public
        if start_on is not None:
            self.start_on = start_on

    @property
    def gid(self):
        """Gets the gid of this ProjectBase.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectBase.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectBase.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectBase.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectBase.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectBase.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this ProjectBase.  # noqa: E501

        Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer.  # noqa: E501

        :return: The name of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectBase.

        Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer.  # noqa: E501

        :param name: The name of this ProjectBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def archived(self):
        """Gets the archived of this ProjectBase.  # noqa: E501

        True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries.  # noqa: E501

        :return: The archived of this ProjectBase.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ProjectBase.

        True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries.  # noqa: E501

        :param archived: The archived of this ProjectBase.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def color(self):
        """Gets the color of this ProjectBase.  # noqa: E501

        Color of the project.  # noqa: E501

        :return: The color of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectBase.

        Color of the project.  # noqa: E501

        :param color: The color of this ProjectBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["dark-pink", "dark-green", "dark-blue", "dark-red", "dark-teal", "dark-brown", "dark-orange", "dark-purple", "dark-warm-gray", "light-pink", "light-green", "light-blue", "light-red", "light-teal", "light-brown", "light-orange", "light-purple", "light-warm-gray", "none", ""]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def created_at(self):
        """Gets the created_at of this ProjectBase.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this ProjectBase.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProjectBase.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this ProjectBase.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def current_status(self):
        """Gets the current_status of this ProjectBase.  # noqa: E501


        :return: The current_status of this ProjectBase.  # noqa: E501
        :rtype: ProjectBaseCurrentStatus
        """
        return self._current_status

    @current_status.setter
    def current_status(self, current_status):
        """Sets the current_status of this ProjectBase.


        :param current_status: The current_status of this ProjectBase.  # noqa: E501
        :type: ProjectBaseCurrentStatus
        """

        self._current_status = current_status

    @property
    def current_status_update(self):
        """Gets the current_status_update of this ProjectBase.  # noqa: E501


        :return: The current_status_update of this ProjectBase.  # noqa: E501
        :rtype: ProjectBaseCurrentStatusUpdate
        """
        return self._current_status_update

    @current_status_update.setter
    def current_status_update(self, current_status_update):
        """Sets the current_status_update of this ProjectBase.


        :param current_status_update: The current_status_update of this ProjectBase.  # noqa: E501
        :type: ProjectBaseCurrentStatusUpdate
        """

        self._current_status_update = current_status_update

    @property
    def custom_field_settings(self):
        """Gets the custom_field_settings of this ProjectBase.  # noqa: E501

        Array of Custom Field Settings (in compact form).  # noqa: E501

        :return: The custom_field_settings of this ProjectBase.  # noqa: E501
        :rtype: list[PortfolioResponseCustomFieldSettings]
        """
        return self._custom_field_settings

    @custom_field_settings.setter
    def custom_field_settings(self, custom_field_settings):
        """Sets the custom_field_settings of this ProjectBase.

        Array of Custom Field Settings (in compact form).  # noqa: E501

        :param custom_field_settings: The custom_field_settings of this ProjectBase.  # noqa: E501
        :type: list[PortfolioResponseCustomFieldSettings]
        """

        self._custom_field_settings = custom_field_settings

    @property
    def default_view(self):
        """Gets the default_view of this ProjectBase.  # noqa: E501

        The default view (list, board, calendar, or timeline) of a project.  # noqa: E501

        :return: The default_view of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._default_view

    @default_view.setter
    def default_view(self, default_view):
        """Sets the default_view of this ProjectBase.

        The default view (list, board, calendar, or timeline) of a project.  # noqa: E501

        :param default_view: The default_view of this ProjectBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["list", "board", "calendar", "timeline"]  # noqa: E501
        if default_view not in allowed_values:
            raise ValueError(
                "Invalid value for `default_view` ({0}), must be one of {1}"  # noqa: E501
                .format(default_view, allowed_values)
            )

        self._default_view = default_view

    @property
    def due_date(self):
        """Gets the due_date of this ProjectBase.  # noqa: E501

        *Deprecated: new integrations should prefer the `due_on` field.*  # noqa: E501

        :return: The due_date of this ProjectBase.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ProjectBase.

        *Deprecated: new integrations should prefer the `due_on` field.*  # noqa: E501

        :param due_date: The due_date of this ProjectBase.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def due_on(self):
        """Gets the due_on of this ProjectBase.  # noqa: E501

        The day on which this project is due. This takes a date with format YYYY-MM-DD.  # noqa: E501

        :return: The due_on of this ProjectBase.  # noqa: E501
        :rtype: date
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this ProjectBase.

        The day on which this project is due. This takes a date with format YYYY-MM-DD.  # noqa: E501

        :param due_on: The due_on of this ProjectBase.  # noqa: E501
        :type: date
        """

        self._due_on = due_on

    @property
    def html_notes(self):
        """Gets the html_notes of this ProjectBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The notes of the project with formatting as HTML.  # noqa: E501

        :return: The html_notes of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._html_notes

    @html_notes.setter
    def html_notes(self, html_notes):
        """Sets the html_notes of this ProjectBase.

        [Opt In](/docs/inputoutput-options). The notes of the project with formatting as HTML.  # noqa: E501

        :param html_notes: The html_notes of this ProjectBase.  # noqa: E501
        :type: str
        """

        self._html_notes = html_notes

    @property
    def members(self):
        """Gets the members of this ProjectBase.  # noqa: E501

        Array of users who are members of this project.  # noqa: E501

        :return: The members of this ProjectBase.  # noqa: E501
        :rtype: list[CustomFieldResponsePeopleValue]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ProjectBase.

        Array of users who are members of this project.  # noqa: E501

        :param members: The members of this ProjectBase.  # noqa: E501
        :type: list[CustomFieldResponsePeopleValue]
        """

        self._members = members

    @property
    def modified_at(self):
        """Gets the modified_at of this ProjectBase.  # noqa: E501

        The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.*  # noqa: E501

        :return: The modified_at of this ProjectBase.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ProjectBase.

        The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.*  # noqa: E501

        :param modified_at: The modified_at of this ProjectBase.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def notes(self):
        """Gets the notes of this ProjectBase.  # noqa: E501

        Free-form textual information associated with the project (ie., its description).  # noqa: E501

        :return: The notes of this ProjectBase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ProjectBase.

        Free-form textual information associated with the project (ie., its description).  # noqa: E501

        :param notes: The notes of this ProjectBase.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def public(self):
        """Gets the public of this ProjectBase.  # noqa: E501

        True if the project is public to its team.  # noqa: E501

        :return: The public of this ProjectBase.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectBase.

        True if the project is public to its team.  # noqa: E501

        :param public: The public of this ProjectBase.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def start_on(self):
        """Gets the start_on of this ProjectBase.  # noqa: E501

        The day on which work for this project begins, or null if the project has no start date. This takes a date with `YYYY-MM-DD` format. *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter. Additionally, `start_on` and `due_on` cannot be the same date.*  # noqa: E501

        :return: The start_on of this ProjectBase.  # noqa: E501
        :rtype: date
        """
        return self._start_on

    @start_on.setter
    def start_on(self, start_on):
        """Sets the start_on of this ProjectBase.

        The day on which work for this project begins, or null if the project has no start date. This takes a date with `YYYY-MM-DD` format. *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter. Additionally, `start_on` and `due_on` cannot be the same date.*  # noqa: E501

        :param start_on: The start_on of this ProjectBase.  # noqa: E501
        :type: date
        """

        self._start_on = start_on

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ProjectBase, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
