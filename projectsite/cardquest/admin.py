from django.contrib import admin


from .models import PokemonCard, Trainer, Collection


@admin.register (PokemonCard)
class PokemonAdmin (admin. ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack", "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities", "image_url", "updated_at", "created_at")
    search_fields = ("name",)

@admin.register (Trainer)
class PokemonAdmin (admin. ModelAdmin):
    list_display = ("name", "birthdate", "location", "email", "updated_at", "created_at")
    search_fields = ("name",)

@admin.register(Collection)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('display_trainer_name', 'display_pokemon_card', 'collection_date', "updated_at", "created_at")
    search_fields = ('trainer__name', 'card__name', 'collection_date__icontains')  

    def display_trainer_name(self, obj):
        return obj.trainer.name if obj.trainer else None

    def display_pokemon_card(self, obj):
        return obj.card.name if obj.card else None

    display_trainer_name.short_description = 'Trainer Name'
    display_pokemon_card.short_description = 'Pokemon Card Name'