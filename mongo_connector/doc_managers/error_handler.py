import re
import logging

from py2neo.database import GraphError as graph_error, BindError as bind_error
from py2neo.database import ClientError as client_error
from py2neo.database import GraphTransactionError as graph_transaction_error
from py2neo.database import DatabaseError as database_error
from py2neo.database import TransientError as transient_error

from mongo_connector import errors
from mongo_connector.errors import OperationFailed


LOG = logging.getLogger(__name__)

class Neo4jOperationFailed(OperationFailed):
    """Raised for failed commands on the destination database
    """
    # print("An error ocurred. Please check mongo-connector.log file")

class ErrorHandler(object):
  def __init__(self):
    self.error_hash = {
    graph_error: Neo4jOperationFailed,
    bind_error: errors.ConnectionFailed,
    database_error: Neo4jOperationFailed,
    graph_transaction_error: Neo4jOperationFailed,
    client_error: Neo4jOperationFailed,
    transient_error: Neo4jOperationFailed,

    AttributeError: Neo4jOperationFailed,
    TypeError: Neo4jOperationFailed,
    NameError: Neo4jOperationFailed,
    RuntimeError: Neo4jOperationFailed

    }
