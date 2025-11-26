
class ResilienceRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Resilience':
            return 'Resilience'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Resilience':
            return 'Resilience'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == 'Resilience' or obj2._state.db == 'analytics':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Resilience':
            return db == 'Resilience'
        return None