"""Generated message classes for datacatalog version v1alpha3.

DataCatalog APIs provides features to attach metadata to Google Cloud Platform
resources like Bigquery Tables.<br> Key critical resources include -<br>     -
Entries  (Datahub representation of a cloud resource)<br>     - Tag Templates
(Definition of columns and value types for attaching metadata)<br>     - Tags
(Values associated with Tag templates and attached to Entries.)<br> Datahub
also provides rich search functionality to search resources for Entries and
tags.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'datacatalog'


class DatacatalogProjectsCrawlersCrawlerRunsGetRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCrawlerRunsGetRequest object.

  Fields:
    name: Required. Resource name of the crawler run to retrieve. For example,
      "projects/project1/crawlers/crawler1/crawlerRuns/run1".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersCrawlerRunsListRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCrawlerRunsListRequest object.

  Fields:
    pageSize: The maximum number of items to return. The default value for
      this field is 10. The maximum value for this field is 1000.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. Resource name of the parent crawler resource. For
      example, "projects/project1/crawlers/crawler1".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersCreateRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersCreateRequest object.

  Fields:
    crawlerId: Required. The id of the crawler to create.
    googleCloudDatacatalogV1alpha3Crawler: A
      GoogleCloudDatacatalogV1alpha3Crawler resource to be passed as the
      request body.
    parent: Required. The name of the project this crawler is in. Example:
      "projects/foo".
  """

  crawlerId = _messages.StringField(1)
  googleCloudDatacatalogV1alpha3Crawler = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersDeleteRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersDeleteRequest object.

  Fields:
    name: Required. The resource name of the crawler. For example,
      "projects/bar/crawlers/foo".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersGetRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersGetRequest object.

  Fields:
    name: Required. The resource name of the crawler. For example,
      "projects/foo/crawlers/bar".
  """

  name = _messages.StringField(1, required=True)


class DatacatalogProjectsCrawlersListRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersListRequest object.

  Fields:
    pageSize: The maximum number of items to return. The default value for
      this field is 10. The maximum value for this field is 1000.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. The parent resource name. Example: "projects/foo".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class DatacatalogProjectsCrawlersPatchRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersPatchRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3Crawler: A
      GoogleCloudDatacatalogV1alpha3Crawler resource to be passed as the
      request body.
    name: Output only. The resource name of the crawler. Must be empty when
      creating a crawler. For example, "projects/a/crawlers/b".
    updateMask: The update mask applies to the resource.
  """

  googleCloudDatacatalogV1alpha3Crawler = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class DatacatalogProjectsCrawlersRunRequest(_messages.Message):
  r"""A DatacatalogProjectsCrawlersRunRequest object.

  Fields:
    googleCloudDatacatalogV1alpha3RunCrawlerRequest: A
      GoogleCloudDatacatalogV1alpha3RunCrawlerRequest resource to be passed as
      the request body.
    name: Required. Resource name of the crawler resource. For example,
      "projects/project1/crawlers/crawler1".
  """

  googleCloudDatacatalogV1alpha3RunCrawlerRequest = _messages.MessageField('GoogleCloudDatacatalogV1alpha3RunCrawlerRequest', 1)
  name = _messages.StringField(2, required=True)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GoogleCloudDatacatalogV1alpha3AdhocRun(_messages.Message):
  r"""Configuration for ad-hoc runs."""


class GoogleCloudDatacatalogV1alpha3BucketScope(_messages.Message):
  r"""Configuration to scope a crawler to the provided list of buckets.

  Fields:
    buckets: The maximum number of buckets allowed is 1000.
  """

  buckets = _messages.MessageField('GoogleCloudDatacatalogV1alpha3BucketSpec', 1, repeated=True)


class GoogleCloudDatacatalogV1alpha3BucketSpec(_messages.Message):
  r"""Configuration for a crawl bucket.

  Fields:
    bucket: The bucket name. For example, GCS bucket name.
  """

  bucket = _messages.StringField(1)


class GoogleCloudDatacatalogV1alpha3Crawler(_messages.Message):
  r"""Crawler Metadata.

  Fields:
    config: Required. The configuration of the crawler.
    description: The description of the crawler.
    displayName: Required. The display name of the crawler.
    name: Output only. The resource name of the crawler. Must be empty when
      creating a crawler. For example, "projects/a/crawlers/b".
  """

  config = _messages.MessageField('GoogleCloudDatacatalogV1alpha3CrawlerConfig', 1)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)
  name = _messages.StringField(4)


class GoogleCloudDatacatalogV1alpha3CrawlerConfig(_messages.Message):
  r"""Crawler configuration.

  Fields:
    adHocRun: Ad-hoc option. User can choose this option for ad-hoc runs.
    bucketScope: Bucket scope. Directs the crawler to crawl specific buckets
      within the project that owns the crawler.
    bundleSpecs: The bundling specifications. Directs the crawler to bundle
      files into filesets based on the bundling specifications.
    organizationScope: Organization scope. Directs the crawler to crawl the
      buckets of the projects in the organization that owns the crawler.
    projectScope: Project scope. Directs the crawler to crawl the buckets of
      the project that owns the crawler.
    scheduledRun: Scheduled option. User can choose this option for scheduled
      runs.
  """

  adHocRun = _messages.MessageField('GoogleCloudDatacatalogV1alpha3AdhocRun', 1)
  bucketScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3BucketScope', 2)
  bundleSpecs = _messages.StringField(3, repeated=True)
  organizationScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ParentOrganizationScope', 4)
  projectScope = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ParentProjectScope', 5)
  scheduledRun = _messages.MessageField('GoogleCloudDatacatalogV1alpha3ScheduledRun', 6)


class GoogleCloudDatacatalogV1alpha3CrawlerRun(_messages.Message):
  r"""A run of the crawler.

  Enums:
    RunOptionValueValuesEnum:
    StateValueValuesEnum: Output only. The state of the crawler run.

  Fields:
    error: Output only. The error status of the crawler run. This field will
      be populated only if the crawler run state is FAILED.
    name: Output only. The name of the crawler run. For example,
      "projects/project1/crawlers/crawler1/crawlerRuns/042423713e9a"
    runOption: A RunOptionValueValuesEnum attribute.
    state: Output only. The state of the crawler run.
  """

  class RunOptionValueValuesEnum(_messages.Enum):
    r"""RunOptionValueValuesEnum enum type.

    Values:
      RUN_OPTION_UNSPECIFIED: Unspecified run option.
      AD_HOC: Ad-hoc run option.
      SCHEDULED: Scheduled run option.
    """
    RUN_OPTION_UNSPECIFIED = 0
    AD_HOC = 1
    SCHEDULED = 2

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The state of the crawler run.

    Values:
      STATE_UNSPECIFIED: Unspecified crawler run state.
      PENDING: This crawler run is waiting on resources to be ready.
      RUNNING: This crawler run is running.
      FAILED: This crawler run failed.
      SUCCEEDED: This crawler run succeeded.
    """
    STATE_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    FAILED = 3
    SUCCEEDED = 4

  error = _messages.MessageField('Status', 1)
  name = _messages.StringField(2)
  runOption = _messages.EnumField('RunOptionValueValuesEnum', 3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class GoogleCloudDatacatalogV1alpha3ListCrawlerRunsResponse(_messages.Message):
  r"""Response to listing the runs from a crawler.

  Fields:
    crawlerRuns: The crawler runs from this crawler, it includes both
      currently running and completed runs.
    nextPageToken: Token to retrieve the next page of results or empty if
      there are no more results in the list.
  """

  crawlerRuns = _messages.MessageField('GoogleCloudDatacatalogV1alpha3CrawlerRun', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudDatacatalogV1alpha3ListCrawlersResponse(_messages.Message):
  r"""Response message for `ListCrawlers` API.

  Fields:
    crawlers: List of crawlers.
    nextPageToken: Token to retrieve the next page of results or empty if
      there are no more results in the list.
  """

  crawlers = _messages.MessageField('GoogleCloudDatacatalogV1alpha3Crawler', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudDatacatalogV1alpha3ParentOrganizationScope(_messages.Message):
  r"""Configuration to scope a crawler to the parent Organization."""


class GoogleCloudDatacatalogV1alpha3ParentProjectScope(_messages.Message):
  r"""Configuration to scope a crawler to the parent project."""


class GoogleCloudDatacatalogV1alpha3RunCrawlerRequest(_messages.Message):
  r"""Request to run a crawler manually."""


class GoogleCloudDatacatalogV1alpha3ScheduledRun(_messages.Message):
  r"""Configuration for scheduled runs.

  Enums:
    ScheduledRunOptionValueValuesEnum: Required. The scheduled run option of
      the crawler.

  Fields:
    scheduledRunOption: Required. The scheduled run option of the crawler.
  """

  class ScheduledRunOptionValueValuesEnum(_messages.Enum):
    r"""Required. The scheduled run option of the crawler.

    Values:
      SCHEDULED_RUN_OPTION_UNSPECIFIED: Unspecified scheduled run option.
      DAILY: Daily scheduled run option.
      WEEKLY: Weekly scheduled run option.
    """
    SCHEDULED_RUN_OPTION_UNSPECIFIED = 0
    DAILY = 1
    WEEKLY = 2

  scheduledRunOption = _messages.EnumField('ScheduledRunOptionValueValuesEnum', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
