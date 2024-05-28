from django.db import models

# Create your models here.
class VehicleData(models.Model):
    vehicle_type = models.CharField(max_length=100)
    vehicle_company = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_plate_number = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=50)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_owner_contact = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type
    
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class AnnotationTypeMaster(models.Model):
    annotation_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annotation_type_master'


class AnprWatchlistDb(models.Model):
    vehicle_number = models.CharField(max_length=80, blank=True, null=True)
    person_name = models.CharField(max_length=80, blank=True, null=True)
    mobile_number = models.CharField(max_length=80, blank=True, null=True)
    make_model = models.CharField(max_length=180, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    vehicle_image = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_category = models.ForeignKey('AnprWlVehicleCategoryMaster', models.DO_NOTHING)
    custom_field = models.JSONField()

    class Meta:
        managed = False
        db_table = 'anpr_watchlist_db'


class AnprWlVehicleCategoryMaster(models.Model):
    vehicle_category = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anpr_wl_vehicle_category_master'


class ApiVehicledata(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=100)
    vehicle_company = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_plate_number = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=50)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_owner_contact = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'api_vehicledata'


class App2FaSessionVerify(models.Model):
    unique_id = models.CharField(max_length=250, blank=True, null=True)
    is_verified = models.BooleanField()
    created_datetime = models.DateTimeField()
    verified_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_2fa_session_verify'


class App2FaUserConfiguration(models.Model):
    enc_auth_key = models.CharField(unique=True, max_length=1800)
    qr_code = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_2fa_user_configuration'


class AppRunningStatusCategoryMaster(models.Model):
    status = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_running_status_category_master'


class ApplicationCategoryMaster(models.Model):
    category_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_category_master'


class ApplicationEventCategoryMaster(models.Model):
    category_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_event_category_master'


class ApplicationProtocolMaster(models.Model):
    protocol_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_protocol_master'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class AutoLabelModelMaster(models.Model):
    model_name = models.CharField(max_length=80, blank=True, null=True)
    model_classes = models.JSONField()
    model_file_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_label_model_master'


class AutoLabelSession(models.Model):
    model_classes = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    model = models.ForeignKey(AutoLabelModelMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_label_session'


class CameraDevice(models.Model):
    device_name = models.CharField(max_length=80, blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    camera_unique_key = models.UUIDField(unique=True)
    camera_url = models.CharField(max_length=300, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    sub_stream_url = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    last_active_datetime = models.DateTimeField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    host_name = models.CharField(max_length=80, blank=True, null=True)
    pass_word = models.CharField(max_length=80, blank=True, null=True)
    user_name = models.CharField(max_length=80, blank=True, null=True)
    protocol = models.ForeignKey('CameraDeviceProtocol', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'camera_device'


class CameraDeviceProtocol(models.Model):
    protocol_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera_device_protocol'


class DailyCountEventStatsSummary(models.Model):
    event_date = models.DateField()
    total_count = models.IntegerField()
    average_count = models.IntegerField()
    peak_count = models.IntegerField()
    off_peak_count = models.IntegerField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)
    event_cam_device = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_class = models.CharField(max_length=200, blank=True, null=True)
    hourly_count = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    stats_updated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_count_event_stats_summary'


class DailyEventStatsSummary(models.Model):
    event_date = models.DateField()
    hourly_count = models.JSONField()
    total_count = models.IntegerField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    stats_updated = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    application = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)
    event_cam_device = models.ForeignKey(CameraDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'daily_event_stats_summary'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoApschedulerDjangojob(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    next_run_time = models.DateTimeField(blank=True, null=True)
    job_state = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojob'


class DjangoApschedulerDjangojobexecution(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=50)
    run_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    finished = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exception = models.CharField(max_length=1000, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    job = models.ForeignKey(DjangoApschedulerDjangojob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojobexecution'
        unique_together = (('job', 'run_time'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailVerification(models.Model):
    passcode = models.CharField(unique=True, max_length=30)
    unique_id = models.CharField(max_length=250, blank=True, null=True)
    is_verified = models.BooleanField()
    verify_type = models.IntegerField()
    password_to_change = models.CharField(max_length=1000)
    created_datetime = models.DateTimeField()
    verified_datetime = models.DateTimeField(blank=True, null=True)
    expire_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_verification'


class FrsWatchlistDb(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=80, blank=True, null=True)
    image = models.JSONField()
    training_status = models.IntegerField()
    is_trained = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    trained_datetime = models.DateTimeField(blank=True, null=True)
    people_category = models.ForeignKey('FrsWlPeopleCategoryMaster', models.DO_NOTHING)
    action_status = models.IntegerField()
    custom_field = models.JSONField()

    class Meta:
        managed = False
        db_table = 'frs_watchlist_db'


class FrsWlPeopleCategoryMaster(models.Model):
    people_category = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frs_wl_people_category_master'


class IntoziAiAnprEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    vehicle_confidence = models.DecimalField(max_digits=10, decimal_places=2)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    plate_bbox = models.JSONField()
    plate_image = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    no_helmet_box = models.JSONField()
    no_seatbelt_box = models.JSONField()
    triple_riding = models.BooleanField(blank=True, null=True)
    driver_on_call_bbox = models.JSONField()
    driver_on_call_status = models.BooleanField(blank=True, null=True)
    no_helmet = models.BooleanField(blank=True, null=True)
    no_seatbelt = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_ANPR_event_data'


class IntoziAiAbandonObjectDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_Abandon_Object_Detection_event_data'


class IntoziAiAdvanceIntrusionDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_Advance_Intrusion_Detection_event_data'


class IntoziAiAnimalCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Animal_count_event_data'


class IntoziAiAxleCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    axle_count = models.CharField(max_length=500, blank=True, null=True)
    vehicle_bbox = models.JSONField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Axle_Count_event_data'


class IntoziAiBaggageCoutingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Baggage_couting_event_data'


class IntoziAiBottleCoutingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Bottle_Couting_event_data'


class IntoziAiCameraTamperingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_class = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Camera_Tampering_event_data'


class IntoziAiColorBasedSearchEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Color_Based_Search_event_data'


class IntoziAiCongestionDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Congestion_Detection_event_data'


class IntoziAiCowCoutingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Cow_couting_event_data'


class IntoziAiCrowdAnomalyDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Anomaly_Detection_event_data'


class IntoziAiCrowdCountManagementEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    crowd_count = models.IntegerField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Count_&_Management_event_data'


class IntoziAiCrowdDispersionDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Dispersion_Detection_event_data'


class IntoziAiCrowdEstimationManagementEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    crowd_count = models.IntegerField()
    percentage_covered = models.DecimalField(max_digits=10, decimal_places=2)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Estimation_&_Management_event_data'


class IntoziAiCrowdFormationEstimationDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Formation_&_Estimation_Detection_event_data'


class IntoziAiCrowdStatisticsHeatmapEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Crowd_Statistics_&_Heatmap_event_data'


class IntoziAiCustomerMovementDominantPathAnalysisEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Customer_Movement_&_Dominant_Path_Analysis_event_data'


class IntoziAiDeadZoneIdentificationEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Dead_Zone_Identification_event_data'


class IntoziAiDetectionOfOversizedVehiclesEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Detection_of_Oversized_Vehicles_event_data'


class IntoziAiDriverSmokingInsideVehicleDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Driver_Smoking_Inside_Vehicle_Detection_event_data'


class IntoziAiDwellTimeEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    dwell_time = models.CharField(max_length=500, blank=True, null=True)
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_Dwell_Time_event_data'


class IntoziAiElephantDetectorEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_bbox = models.JSONField()
    event_class = models.CharField(max_length=500, blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Elephant_Detector_event_data'


class IntoziAiEncroachmentDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Encroachment_Detection_event_data'


class IntoziAiFaceRecognitionFrEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    frs_box = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    similarity_confidence = models.DecimalField(max_digits=10, decimal_places=2)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Face_Recognition_(FR)_event_data'


class IntoziAiFenceJumpingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    people_bbox = models.JSONField()
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Fence_Jumping_event_data'


class IntoziAiGarbageBinDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Garbage_Bin_Detection_event_data'


class IntoziAiGarbageBinEmptiedDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Garbage_Bin_Emptied_Detection_event_data'


class IntoziAiHazardousAreaEntryDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    object_box = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Hazardous_Area_Entry_Detection_event_data'


class IntoziAiIncidentDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Incident_Detection_event_data'


class IntoziAiInventoryCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Inventory_count_event_data'


class IntoziAiLineCrossingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_Line_Crossing_event_data'


class IntoziAiLitterDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Litter_Detection_event_data'


class IntoziAiLoadingAndUnloadingMonitoringEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Loading_and_Unloading_Monitoring_event_data'


class IntoziAiLoiteringEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    object_box = models.JSONField()
    roi_id = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Loitering_event_data'


class IntoziAiMobGatheringEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    count = models.IntegerField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Mob_Gathering_event_data'


class IntoziAiMobileDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_bbox = models.JSONField()
    event_class = models.CharField(max_length=500, blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Mobile_Detection_event_data'


class IntoziAiMobileTalkingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Mobile_Talking_event_data'


class IntoziAiNoHelmetViolationEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    track_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_No_Helmet_Violation_event_data'


class IntoziAiNoSeatbeltEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    plate_bbox = models.JSONField()
    plate_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_confidence = models.DecimalField(max_digits=10, decimal_places=2)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_No_Seatbelt_event_data'


class IntoziAiObjectCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Object_count_event_data'


class IntoziAiPpeDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    object_bbox = models.JSONField()
    object_class = models.CharField(max_length=500, blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    ppe_bbox = models.JSONField()
    ppe_class = models.CharField(max_length=500, blank=True, null=True)
    ppe_no_bbox = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_PPE_Detection_event_data'


class IntoziAiPeopleCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    count = models.IntegerField()
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_Count_event_data'


class IntoziAiPeopleFallDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    people_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_Fall_Detection_event_data'


class IntoziAiPeopleFightingViolenceEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_Fighting/Violence_event_data'


class IntoziAiPeopleInOutEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    direction = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    object_box = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_IN/OUT_event_data'


class IntoziAiPeopleTrackingTrajectoryEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_Tracking_&_Trajectory_event_data'


class IntoziAiPeopleCountingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_People_counting_event_data'


class IntoziAiPerimeterDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Perimeter_Detection_event_data'


class IntoziAiPlantCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Plant_count_event_data'


class IntoziAiPoorVisibiltyEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Poor_Visibilty_event_data'


class IntoziAiQueueLimitExceedDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Queue_Limit_Exceed_Detection_event_data'


class IntoziAiRedLightStopLineViolationDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Red_Light_&_Stop_Line_Violation_Detection_event_data'


class IntoziAiRegionEntranceExitingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    object_box = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    direction = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Region_Entrance/Exiting_event_data'


class IntoziAiSafetyJacketDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Safety_jacket_Detection_event_data'


class IntoziAiScratchDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Scratch_Detection_event_data'


class IntoziAiSheepCountingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Sheep_counting_event_data'


class IntoziAiSlowMovingVehicleEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    track_id = models.CharField(max_length=500, blank=True, null=True)
    vehicle_bbox = models.JSONField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Slow_Moving_Vehicle_event_data'


class IntoziAiSmokeFireEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    event_bbox = models.JSONField()
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    event_class = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Smoke_&_Fire_event_data'


class IntoziAiStockCountEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Stock_count_event_data'


class IntoziAiStoppedVehicleOrBrokenDownEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    track_id = models.CharField(max_length=500, blank=True, null=True)
    vehicle_bbox = models.JSONField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Stopped_Vehicle_or_Broken-Down_event_data'


class IntoziAiStoppedOrBrokenDownVehicleOnRoadEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Stopped_or_Broken-Down_Vehicle_on_Road_event_data'


class IntoziAiStrayAnimalDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_bbox = models.JSONField()
    event_class = models.CharField(max_length=500, blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Stray_Animal_Detection_event_data'


class IntoziAiTrafficVolumeEstimationEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_count = models.IntegerField()
    percentage_covered = models.DecimalField(max_digits=10, decimal_places=2)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Traffic_Volume_Estimation_event_data'


class IntoziAiTrainDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_bbox = models.JSONField()
    event_class = models.CharField(max_length=500, blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Train_Detection_event_data'


class IntoziAiTyreCoutingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Tyre_couting_event_data'


class IntoziAiUnattendedObjectEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    roi_id = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Unattended_Object_event_data'


class IntoziAiVandalismEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vandalism_event_data'


class IntoziAiVehicleColorDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vehicle_Color_Detection_event_data'


class IntoziAiVehicleQueueLengthEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vehicle_Queue_Length_event_data'


class IntoziAiVehicleSpeedEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_bbox = models.JSONField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    driver_on_call_bbox = models.JSONField()
    no_helmet = models.BooleanField(blank=True, null=True)
    no_helmet_box = models.JSONField()
    no_seatbelt = models.BooleanField(blank=True, null=True)
    no_seatbelt_box = models.JSONField()
    plate_bbox = models.JSONField()
    plate_image = models.CharField(max_length=500, blank=True, null=True)
    stopped_vehicle = models.BooleanField(blank=True, null=True)
    triple_bbox = models.JSONField()
    triple_riding = models.BooleanField(blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    vehicle_speed = models.CharField(max_length=500, blank=True, null=True)
    driver_on_call = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vehicle_Speed_event_data'


class IntoziAiVehicleTrajectoryHeatMapEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    track_id = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    centroids = models.JSONField()
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    roi_id = models.IntegerField()
    end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vehicle_Trajectory_&_Heat_Map_event_data'


class IntoziAiVehicleCountingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    roi_id = models.IntegerField()
    tracking_id = models.IntegerField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Vehicle_counting_event_data'


class IntoziAiWaitTimeInAQueueLiftLobbyEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Wait_Time_in_a_Queue/Lift_Lobby_event_data'


class IntoziAiWomanSafetyEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Woman_Safety_event_data'


class IntoziAiWorkerBehaviourMonitoringEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Worker_Behaviour_Monitoring_event_data'


class IntoziAiWrongLaneEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    plate_bbox = models.JSONField()
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Wrong_Lane_event_data'


class IntoziAiWrongParkEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    stay_time = models.CharField(max_length=500, blank=True, null=True)
    plate_bbox = models.JSONField()
    anpr_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_bbox = models.JSONField()
    track_id = models.CharField(max_length=500, blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    vehicle_confidence = models.DecimalField(max_digits=10, decimal_places=2)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Wrong_Park_event_data'


class IntoziAiWrongWayEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    vehicle_bbox = models.JSONField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    vehicle_class = models.CharField(max_length=500, blank=True, null=True)
    plate_bbox = models.JSONField()
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Wrong_Way_event_data'


class IntoziAiZigZagDrivingDetectionEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_Zig_Zag_Driving_Detection_event_data'


class IntoziAiAlertAlertDeliveryLogs(models.Model):
    alert_message = models.JSONField()
    iaadl_alert_event_id = models.IntegerField()
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    iaadl_alert_category = models.ForeignKey('IntoziAiAlertCategory', models.DO_NOTHING)
    iaadl_alert_group = models.ForeignKey('IntoziAiAlertGroup', models.DO_NOTHING)
    iaadl_alert_status = models.ForeignKey('IntoziAiAlertDeliveryStatusMaster', models.DO_NOTHING)
    iaadl_application = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)
    iaadl_camera = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    iaadl_watchlist = models.ForeignKey('IntoziAiWatchlist', models.DO_NOTHING)
    alert_recipients = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_alert_delivery_logs'


class IntoziAiAlertCategory(models.Model):
    alert_category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_category'


class IntoziAiAlertDeliveryStatusMaster(models.Model):
    alert_delivery_status = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_delivery_status_master'


class IntoziAiAlertGroup(models.Model):
    group_name = models.CharField(max_length=50, blank=True, null=True)
    group_description = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    alert_category = models.ForeignKey(IntoziAiAlertCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_group'


class IntoziAiAlertMaster(models.Model):
    alert_name = models.CharField(max_length=50, blank=True, null=True)
    alert_schema = models.JSONField()
    icon_path = models.CharField(max_length=300, blank=True, null=True)
    integration_document = models.CharField(max_length=300, blank=True, null=True)
    provider = models.CharField(max_length=50, blank=True, null=True)
    alert_category = models.ForeignKey(IntoziAiAlertCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_master'


class IntoziAiAlertSessionConfig(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    alert_config = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    alert_type = models.ForeignKey(IntoziAiAlertMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_session_config'


class IntoziAiAlertUserDetailMaster(models.Model):
    person_name = models.CharField(max_length=50, blank=True, null=True)
    contact_info = models.CharField(max_length=80, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    alert_group = models.ForeignKey(IntoziAiAlertGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_alert_user_detail_master'


class IntoziAiAppEventConsumerConfigMaster(models.Model):
    consumer_config_name = models.CharField(max_length=50, blank=True, null=True)
    config_headers = models.JSONField()
    synch_duration = models.IntegerField()
    config_description = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    is_enabled = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    event_consumer_category = models.ForeignKey('IntoziApplicationEventConsumerCategory', models.DO_NOTHING)
    updated_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_event_consumer_config_master'


class IntoziAiAppEventConsumerConfigMasterConumerApplications(models.Model):
    intoziaiapplicationeventconsumerconfigmaster = models.ForeignKey(IntoziAiAppEventConsumerConfigMaster, models.DO_NOTHING)
    intoziaiapplicationmaster = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_event_consumer_config_master_conumer_applications'
        unique_together = (('intoziaiapplicationeventconsumerconfigmaster', 'intoziaiapplicationmaster'),)


class IntoziAiAppEventCountUpdateLogs(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_event_count_update_logs'


class IntoziAiAppFlowConfig(models.Model):
    app_flow_config_name = models.CharField(max_length=50, blank=True, null=True)
    app_flow_config = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    is_enabled = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    app_id = models.ForeignKey('IntoziAiApplicationMaster', models.DO_NOTHING)
    container_port = models.IntegerField()
    running_status = models.ForeignKey(AppRunningStatusCategoryMaster, models.DO_NOTHING)
    updated_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_flow_config'


class IntoziAiAppModelClassMaster(models.Model):
    class_uuid_id = models.UUIDField(unique=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    class_description = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_model_class_master'


class IntoziAiAppModelMaster(models.Model):
    model_uuid_id = models.UUIDField(unique=True)
    model_name = models.CharField(max_length=50, blank=True, null=True)
    model_description = models.CharField(max_length=500, blank=True, null=True)
    model_file_name = models.CharField(max_length=50, blank=True, null=True)
    model_base_path = models.CharField(max_length=500, blank=True, null=True)
    parameters = models.JSONField()
    model_config_parameters = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_model_master'


class IntoziAiAppModelMasterModelClasses(models.Model):
    intoziaiappmodelmaster = models.ForeignKey(IntoziAiAppModelMaster, models.DO_NOTHING)
    intoziaimodelclassmaster = models.ForeignKey(IntoziAiAppModelClassMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_app_model_master_model_classes'
        unique_together = (('intoziaiappmodelmaster', 'intoziaimodelclassmaster'),)


class IntoziAiApplicationMaster(models.Model):
    application_name = models.CharField(max_length=50, blank=True, null=True)
    app_variant_name = models.CharField(max_length=50, blank=True, null=True)
    app_description = models.CharField(max_length=500, blank=True, null=True)
    app_logo = models.CharField(max_length=500, blank=True, null=True)
    app_version = models.CharField(max_length=25, blank=True, null=True)
    app_config_parameters = models.JSONField()
    is_subscribed = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    app_id = models.IntegerField()
    app_models = models.JSONField()
    app_output_schema = models.JSONField()
    app_event_field_master = models.JSONField()
    app_repo = models.CharField(max_length=200, blank=True, null=True)
    application_category = models.ForeignKey(ApplicationCategoryMaster, models.DO_NOTHING)
    watchlist_db = models.BooleanField(blank=True, null=True)
    watchlist_schema = models.JSONField()
    application_event_category = models.ForeignKey(ApplicationEventCategoryMaster, models.DO_NOTHING)
    is_event_synching = models.BooleanField(blank=True, null=True)
    event_filter = models.JSONField()
    app_consumer_key = models.CharField(max_length=50, blank=True, null=True)
    application_db_name = models.CharField(max_length=80, blank=True, null=True)
    subscribed_engines = models.JSONField()
    event_deletion = models.BooleanField(blank=True, null=True)
    consumer_alert_type = models.IntegerField()
    application_stats_attributes = models.JSONField()
    roi_dependancy = models.BooleanField(blank=True, null=True)
    event_update = models.BooleanField(blank=True, null=True)
    event_update_fields = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_application_master'


class IntoziAiApplicationMasterDeviceManager(models.Model):
    intoziaiapplicationmaster = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    cameradevice = models.ForeignKey(CameraDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_application_master_device_manager'
        unique_together = (('intoziaiapplicationmaster', 'cameradevice'),)


class IntoziAiApplicationScheduler(models.Model):
    week_interval = models.JSONField()
    interval_start_time = models.TimeField()
    interval_end_time = models.TimeField()
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    application_config = models.ForeignKey(IntoziAiAppFlowConfig, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_application_scheduler'


class IntoziAiCameraDeviceHealth(models.Model):
    health_active_status = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    cam_device = models.ForeignKey(CameraDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_camera_device_health'


class IntoziAiCameraRoiConfig(models.Model):
    roi_name = models.CharField(max_length=80, blank=True, null=True)
    roi_config = models.JSONField()
    roi_color = models.CharField(max_length=80, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    ai_app = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    cam_device = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    roi_type = models.ForeignKey('IntoziAiRoiTypeMaster', models.DO_NOTHING)
    roi_direction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_camera_roi_config'


class IntoziAiCookiesCountingEventData(models.Model):
    is_deleted = models.BooleanField(blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)
    event_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_cookies_counting_event_data'


class IntoziAiDailyEventCountLogs(models.Model):
    event_date = models.DateField()
    total_event_count = models.IntegerField()
    application_count = models.JSONField()
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_daily_event_count_logs'


class IntoziAiEventCountLogs(models.Model):
    event_count = models.IntegerField()
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    month_interval_count = models.JSONField()
    device_count = models.JSONField()
    week_interval_count = models.JSONField()
    yearly_interval_count = models.JSONField()
    hourly_interval_count = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    event_severity_count = models.JSONField()
    alert_delivery_count = models.JSONField()
    off_peak_hour = models.JSONField()
    peak_hour = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_event_count_logs'


class IntoziAiEventServerSyncLogs(models.Model):
    server_response = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    consumer = models.ForeignKey(IntoziAiAppEventConsumerConfigMaster, models.DO_NOTHING)
    synch_status = models.ForeignKey('IntoziAiEventSynchStatusMaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_event_server_sync_logs'


class IntoziAiEventSynchStatusMaster(models.Model):
    status = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_event_synch_status_master'


class IntoziAiFieldTypeMaster(models.Model):
    field_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_field_type_master'


class IntoziAiMetaParametersConfig(models.Model):
    node_type_name = models.CharField(max_length=50, blank=True, null=True)
    successor = models.JSONField()
    predecessor = models.JSONField()
    is_required = models.BooleanField(blank=True, null=True)
    is_unique = models.BooleanField(blank=True, null=True)
    node_params = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_meta_parameters_config'


class IntoziAiModelArchitectureMaster(models.Model):
    architecture_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_model_architecture_master'


class IntoziAiRoiTypeMaster(models.Model):
    type_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_roi_type_master'


class IntoziAiServerConfigManager(models.Model):
    host_name = models.CharField(max_length=80, blank=True, null=True)
    port = models.IntegerField()
    server_auth_key = models.CharField(max_length=180, blank=True, null=True)
    server_health = models.JSONField()
    server_details = models.JSONField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField(blank=True, null=True)
    protocol = models.ForeignKey(ApplicationProtocolMaster, models.DO_NOTHING)
    server_type = models.ForeignKey('ServerTypeMaster', models.DO_NOTHING)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    server_unique_key = models.UUIDField(unique=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_server_config_manager'


class IntoziAiSuitConfiguration(models.Model):
    configuration_name = models.CharField(max_length=80, blank=True, null=True)
    configuration_master = models.JSONField()
    configuration_data = models.JSONField()
    configuration_action = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_suit_configuration'


class IntoziAiSuitFrsEventData(models.Model):
    frs_box = models.JSONField()
    similarity_confidence = models.DecimalField(max_digits=10, decimal_places=2)
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    user_id = models.ForeignKey(FrsWatchlistDb, models.DO_NOTHING, blank=True, null=True)
    roi_id = models.IntegerField()
    event_roi = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField()
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey(IntoziAiEventSynchStatusMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_suit_frs_event_data'


class IntoziAiSuitFrsUnregEventData(models.Model):
    uq_id = models.UUIDField(unique=True)
    frs_box = models.JSONField()
    roi_id = models.IntegerField()
    event_image = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    is_img_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    cam_id = models.ForeignKey(CameraDevice, models.DO_NOTHING)
    confidence = models.DecimalField(max_digits=10, decimal_places=2)
    event_roi = models.CharField(max_length=500, blank=True, null=True)
    is_synched = models.BooleanField(blank=True, null=True)
    event_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    synch_status = models.ForeignKey(IntoziAiEventSynchStatusMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_suit_frs_unreg_event_data'


class IntoziAiSuiteApiIntoziaianprmodel(models.Model):

    class Meta:
        managed = False
        db_table = 'intozi_ai_suite_api_intoziaianprmodel'


class IntoziAiSuiteApiIntoziaianprmodel1(models.Model):

    class Meta:
        managed = False
        db_table = 'intozi_ai_suite_api_intoziaianprmodel1'


class IntoziAiSuiteWallGroup(models.Model):
    group_name = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_suite_wall_group'


class IntoziAiSuiteWallGroupCameraDevice(models.Model):
    intoziaisuitewallgroup = models.ForeignKey(IntoziAiSuiteWallGroup, models.DO_NOTHING)
    cameradevice = models.ForeignKey(CameraDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_suite_wall_group_camera_device'
        unique_together = (('intoziaisuitewallgroup', 'cameradevice'),)


class IntoziAiWatchlist(models.Model):
    watchlist_name = models.CharField(max_length=80, blank=True, null=True)
    camera = models.JSONField()
    alert_enabled = models.BooleanField(blank=True, null=True)
    is_enabled = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    wl_alert_category = models.ForeignKey(IntoziAiAlertMaster, models.DO_NOTHING)
    wl_alert_config = models.ForeignKey(IntoziAiAlertSessionConfig, models.DO_NOTHING)
    wl_alert_user_config = models.ForeignKey(IntoziAiAlertGroup, models.DO_NOTHING)
    wl_app = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)
    wl_app_flow_config = models.ForeignKey(IntoziAiAppFlowConfig, models.DO_NOTHING)
    wl_severity = models.ForeignKey('IntoziAiWlSeverityLevelMaster', models.DO_NOTHING)
    wl_description = models.CharField(max_length=500, blank=True, null=True)
    alert_notification = models.BooleanField(blank=True, null=True)
    sound_alert = models.BooleanField(blank=True, null=True)
    wl_alert_recurrency_type = models.ForeignKey('IntoziAiWlRecurrentTypeMaster', models.DO_NOTHING)
    wl_alert_recurrency_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'intozi_ai_watchlist'


class IntoziAiWatchlistDbDataMaster(models.Model):
    db_data_master_name = models.CharField(max_length=80, blank=True, null=True)
    is_enabled = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    wl_db_dm_app = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_ai_watchlist_db_data_master'


class IntoziAiWlCategory(models.Model):
    wl_category_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_wl_category'


class IntoziAiWlRecurrentTypeMaster(models.Model):
    recurrent_type = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_wl_recurrent_type_master'


class IntoziAiWlSeverityLevelMaster(models.Model):
    severity_level = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_ai_wl_severity_level_master'


class IntoziAimtProject(models.Model):
    iamtp_uuid_id = models.UUIDField(unique=True)
    project_name = models.CharField(max_length=50, blank=True, null=True)
    project_label = models.CharField(max_length=50, blank=True, null=True)
    project_description = models.CharField(max_length=500, blank=True, null=True)
    project_color_code = models.CharField(max_length=6)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    project_data_paths = models.JSONField()
    annotation_type = models.ForeignKey(AnnotationTypeMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_aimt_project'


class IntoziAimtProjectClass(models.Model):
    class_name = models.CharField(max_length=50, blank=True, null=True)
    class_theme_color = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intozi_aimt_project_class'


class IntoziAimtProjectClasses(models.Model):
    intoziaimtproject = models.ForeignKey(IntoziAimtProject, models.DO_NOTHING)
    intoziaimtprojectclasses = models.ForeignKey(IntoziAimtProjectClass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_aimt_project_classes'
        unique_together = (('intoziaimtproject', 'intoziaimtprojectclasses'),)


class IntoziApplicationEventConsumerCategory(models.Model):
    category_name = models.CharField(max_length=80, blank=True, null=True)
    config_json = models.JSONField()

    class Meta:
        managed = False
        db_table = 'intozi_application_event_consumer_category'


class IntoziDbBackupSynchLog(models.Model):
    db_backup_file_name = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'intozi_db_backup_synch_log'


class IntoziEmail2FaSessionVerify(models.Model):
    passcode = models.CharField(unique=True, max_length=30)
    unique_id = models.CharField(max_length=250, blank=True, null=True)
    is_verified = models.BooleanField()
    created_datetime = models.DateTimeField()
    verified_datetime = models.DateTimeField(blank=True, null=True)
    expire_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intozi_email_2fa_session_verify'


class License(models.Model):
    license_data = models.CharField(max_length=5000)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license'


class ReportDownloadFormatMaster(models.Model):
    report_type = models.CharField(max_length=80, blank=True, null=True)
    report_format = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_download_format_master'


class ServerTypeMaster(models.Model):
    server_type = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_type_master'


class TwoFactorAuthenticationType(models.Model):
    authentication_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'two_factor_authentication_type'


class UserPermissions(models.Model):
    permission_name = models.CharField(max_length=300)
    permission_action = models.JSONField()
    permission_logo = models.CharField(max_length=300)
    permission_key = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'user_permissions'


class UserRoles(models.Model):
    role_name = models.CharField(unique=True, max_length=300)
    role_description = models.CharField(unique=True, max_length=800)
    created_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_roles'


class UserSessionManager(models.Model):
    client_user_agent = models.CharField(max_length=800, blank=True, null=True)
    client_ip = models.CharField(max_length=100, blank=True, null=True)
    client_platform = models.CharField(max_length=100, blank=True, null=True)
    login_datetime = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    user_session_id = models.ForeignKey('Users', models.DO_NOTHING)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_session_manager'


class UserType(models.Model):
    type_name = models.CharField(unique=True, max_length=30)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    user_role = models.ForeignKey(UserRoles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_type'


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(unique=True, max_length=250, blank=True, null=True)
    admin_key = models.CharField(unique=True, max_length=250, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    active = models.BooleanField()
    staff = models.BooleanField()
    admin = models.BooleanField()
    mobile_number = models.CharField(max_length=15)
    user_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    is_2fa_enabled = models.BooleanField(blank=True, null=True)
    super_user_id = models.IntegerField()
    roles_defined = models.BooleanField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateTimeField(blank=True, null=True)
    authentication_type = models.ForeignKey(TwoFactorAuthenticationType, models.DO_NOTHING)
    user_type = models.ForeignKey(UserType, models.DO_NOTHING)
    is_verified = models.BooleanField()
    user_color_code = models.CharField(max_length=6)
    is_synched = models.BooleanField(blank=True, null=True)
    account_status = models.IntegerField()
    user_permissions = models.JSONField()

    class Meta:
        managed = False
        db_table = 'users'


class WatchlistDbCustomField(models.Model):
    fields_schema = models.JSONField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(IntoziAiApplicationMaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'watchlist_db_custom_field'
