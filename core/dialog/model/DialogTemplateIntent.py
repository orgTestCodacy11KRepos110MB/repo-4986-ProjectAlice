from dataclasses import dataclass, field


@dataclass
class DialogTemplateIntent:
	name: str
	description: str
	enabledByDefault: bool
	utterances: list = field(default_factory=list)
	slots: list = field(default_factory=list)


	def dump(self) -> dict:
		return {
			'name'            : f'{self.name}',
			'description'     : f'{self.description}',
			'enabledByDefault': f'{self.enabledByDefault}',
			'utterances'      : f'{self.utterances}',
			'slots'           : f'{self.slots}'
		}
