# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.link import Link  # noqa: F401,E501
from swagger_server.models.node import Node  # noqa: F401,E501
from swagger_server.models.service import Service  # noqa: F401,E501
from swagger_server import util


class Topology(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, domain_service: Service=None, version: int=None, time_stamp: datetime=None, nodes: List[Node]=None, links: List[Link]=None, private_attributes: List[str]=None):  # noqa: E501
        """Topology - a model defined in Swagger

        :param id: The id of this Topology.  # noqa: E501
        :type id: str
        :param name: The name of this Topology.  # noqa: E501
        :type name: str
        :param domain_service: The domain_service of this Topology.  # noqa: E501
        :type domain_service: Service
        :param version: The version of this Topology.  # noqa: E501
        :type version: int
        :param time_stamp: The time_stamp of this Topology.  # noqa: E501
        :type time_stamp: datetime
        :param nodes: The nodes of this Topology.  # noqa: E501
        :type nodes: List[Node]
        :param links: The links of this Topology.  # noqa: E501
        :type links: List[Link]
        :param private_attributes: The private_attributes of this Topology.  # noqa: E501
        :type private_attributes: List[str]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'domain_service': Service,
            'version': int,
            'time_stamp': datetime,
            'nodes': List[Node],
            'links': List[Link],
            'private_attributes': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'domain_service': 'domain_service',
            'version': 'version',
            'time_stamp': 'time_stamp',
            'nodes': 'nodes',
            'links': 'links',
            'private_attributes': 'private_attributes'
        }
        self._id = id
        self._name = name
        self._domain_service = domain_service
        self._version = version
        self._time_stamp = time_stamp
        self._nodes = nodes
        self._links = links
        self._private_attributes = private_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Topology':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The topology of this Topology.  # noqa: E501
        :rtype: Topology
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Topology.


        :return: The id of this Topology.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Topology.


        :param id: The id of this Topology.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Topology.


        :return: The name of this Topology.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Topology.


        :param name: The name of this Topology.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain_service(self) -> Service:
        """Gets the domain_service of this Topology.


        :return: The domain_service of this Topology.
        :rtype: Service
        """
        return self._domain_service

    @domain_service.setter
    def domain_service(self, domain_service: Service):
        """Sets the domain_service of this Topology.


        :param domain_service: The domain_service of this Topology.
        :type domain_service: Service
        """

        self._domain_service = domain_service

    @property
    def version(self) -> int:
        """Gets the version of this Topology.


        :return: The version of this Topology.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """Sets the version of this Topology.


        :param version: The version of this Topology.
        :type version: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def time_stamp(self) -> datetime:
        """Gets the time_stamp of this Topology.


        :return: The time_stamp of this Topology.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: datetime):
        """Sets the time_stamp of this Topology.


        :param time_stamp: The time_stamp of this Topology.
        :type time_stamp: datetime
        """
        if time_stamp is None:
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        self._time_stamp = time_stamp

    @property
    def nodes(self) -> List[Node]:
        """Gets the nodes of this Topology.


        :return: The nodes of this Topology.
        :rtype: List[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: List[Node]):
        """Sets the nodes of this Topology.


        :param nodes: The nodes of this Topology.
        :type nodes: List[Node]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def links(self) -> List[Link]:
        """Gets the links of this Topology.


        :return: The links of this Topology.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links: List[Link]):
        """Sets the links of this Topology.


        :param links: The links of this Topology.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def private_attributes(self) -> List[str]:
        """Gets the private_attributes of this Topology.


        :return: The private_attributes of this Topology.
        :rtype: List[str]
        """
        return self._private_attributes

    @private_attributes.setter
    def private_attributes(self, private_attributes: List[str]):
        """Sets the private_attributes of this Topology.


        :param private_attributes: The private_attributes of this Topology.
        :type private_attributes: List[str]
        """

        self._private_attributes = private_attributes
