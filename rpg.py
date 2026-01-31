def create_character(Name, Strength, Intelligence, Charisma):  # ← Capitalized parameters
    # Character name validation
    if not isinstance(Name, str):  # ← Capitalized
        return "The character name should be a string"
    
    if Name == "":  # ← Capitalized
        return "The character should have a name"
    
    if len(Name) > 10:  # ← Capitalized
        return "The character name is too long"
    
    if " " in Name:  # ← Capitalized
        return "The character name should not contain spaces"
    
    # Stats validation
    stats = [Strength, Intelligence, Charisma]  # ← All capitalized
    
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    # Create output
    output_lines = [Name]  # ← Capitalized
    
    stat_data = [('STR', Strength), ('INT', Intelligence), ('CHA', Charisma)]
    #                        ^ Capitalized        ^ Capitalized         ^ Capitalized
    
    for stat_name, value in stat_data:
        full_dots = "●" * value
        empty_dots = "○" * (10 - value)
        line = f'{stat_name} {full_dots}{empty_dots}'
        output_lines.append(line)
    
    return '\n'.join(output_lines)
