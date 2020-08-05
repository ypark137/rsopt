from rsopt.configuration import Settings, Parameters, get_reader


class Optimizer:
    def __init__(self):
        self.gen_specs = {}
        self.dimension = 0
        self.optimizer_method = ''
        self.options = {}
        self.settings = Settings()
        self.parameters = Parameters()
        self.exit_criteria = None
        self.function = None
        self.executable = None

    @property
    def lb(self):
        return self.parameters.get_lower_bound()

    @lb.setter
    def lb(self, value=None):
        pass

    @property
    def ub(self):
        return self.parameters.get_upper_bound()

    @ub.setter
    def ub(self, value=None):
        pass

    @property
    def start(self):
        return self.parameters.get_start()

    @start.setter
    def start(self, value=None):
        pass

    def _set_dimension(self):
        if len(self.parameters.pararameters) == 0:
            print("Warning: Cannot set dimension. No parameters have been set.")
        else:
            self.dimension = len(self.parameters.pararameters)

    def set_parameters(self, parameters):
        reader = get_reader(parameters, 'parameters')
        for name, values in reader(parameters):
            self.parameters.parse_parameters(name, values)

    def set_settings(self, settings):
        reader = get_reader(settings, 'settings')
        for name, value in reader(settings):
            self.settings.parse_settings(name, value)

    def set_exit_criteria(self, exit_criteria):
        # TODO: Will override in sublcasses probably
        self.exit_criteria = exit_criteria