
class Validator:
    def __init__(self, ast):
        self.ast = ast
        self.errors = []

    def validate_motifs(self):
        """Ensure that only valid structural motifs are defined."""
        for section, elements in self.ast["sections"].items():
            if section == "STRUCTURE":
                for motif in elements:
                    if motif not in VALID_MOTIFS:
                        self.errors.append(f"Invalid motif: {motif}")
    
    def validate_linkages(self):
        """Ensure that linkages connect valid motifs."""
        for section, elements in self.ast["sections"].items():
            if section == "LINKAGES":
                for linkage in elements:
                    if isinstance(linkage, dict):
                        linkage_name, connected_motifs = list(linkage.items())[0]
                        if linkage_name not in VALID_LINKAGES:
                            self.errors.append(f"Invalid linkage: {linkage_name}")
                        else:
                            expected_types = VALID_LINKAGES[linkage_name]
                            actual_types = [motif[:3] for motif in connected_motifs]  # Extract first 3 chars for type
                            if tuple(actual_types) != expected_types:
                                self.errors.append(f"Invalid linkage {linkage_name}: Expected {expected_types}, got {actual_types}")

    def run(self):
        self.validate_motifs()
        self.validate_linkages()
        if self.errors:
            for error in self.errors:
                print(f"Validation Error: {error}")
        else:
            print("Validation successful! No issues found.")

# Example usage
validator = Validator(ast)
validator.run()
