# -*- coding: utf-8 -*-
from pyramid.events import subscriber
from pyramid.events import ContextFound
from openregistry.api.events import ErrorDesctiptorEvent
from openregistry.api.utils import update_logging_context


@subscriber(ErrorDesctiptorEvent)
def tender_error_handler(event):
    if 'asset' in event.request.validated:
        event.params['ASSET_REV'] = event.request.validated['asset'].rev
        event.params['ASSETID'] = event.request.validated['asset'].assetID
        event.params['ASSET_STATUS'] = event.request.validated['asset'].status


@subscriber(ContextFound)
def extend_asset_logging_context(event):
    request = event.request
    if 'asset' in request.validated:
        params = dict()
        params['ASSET_REV'] = request.validated['asset'].rev
        params['ASSETID'] = request.validated['asset'].assetID
        params['ASSET_STATUS'] = request.validated['asset'].status
        update_logging_context(request, params)
