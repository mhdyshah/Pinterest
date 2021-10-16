from rest_framework import serializers

from personalsettings.models import PublicProfile, AccountSettings


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicProfile
        fields = (
            "id", "updated_by", "updated_at", "fullname", "username", "shortBio", "photo", "pronouns", "website", "age"
        )
        read_only_fields = ("id", "updated_by",)


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = (
            "id", "updated_by", "updated_at", "email", "password", "country", "language", "gender"
        )
        read_only_fields = ("id", "updated_by", "updated_at")
