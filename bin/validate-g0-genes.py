#!/usr/bin/env python3
"""
Validate g0-locus genes against the inseparable-knife principle.

Usage: python3 bin/validate-g0-genes.py dialectic/invariants-bond.yaml

Flags nodes with locus: g0 that lack observability or grounded_in sections.
Advisory only — not a hard gate. See dialectic/g0-gene-checklist.md for context.
"""

import sys
import yaml

def validate_g0_genes(yaml_path):
    """Load YAML and check all g0 nodes."""

    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {yaml_path} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)

    invariants = data.get('invariants', [])
    g0_nodes = [inv for inv in invariants if inv.get('locus') == 'g0']

    if not g0_nodes:
        print("✓ No g0 nodes found.")
        return 0

    print(f"Found {len(g0_nodes)} g0-locus nodes.\n")

    issues = []

    for node in g0_nodes:
        node_id = node.get('id', '<unnamed>')
        missing = []

        # Check observability
        observability = node.get('observability')
        if not observability:
            missing.append("observability (breach detection)")
        elif isinstance(observability, dict):
            if not observability.get('breach_example'):
                missing.append("observability.breach_example")

        # Check grounded_in
        grounded_in = node.get('grounded_in')
        if not grounded_in:
            missing.append("grounded_in (justification)")
        elif isinstance(grounded_in, list) and len(grounded_in) == 0:
            missing.append("grounded_in (empty list)")

        if missing:
            issues.append({
                'id': node_id,
                'missing': missing,
                'one_liner': node.get('one_liner', '<no one_liner>')
            })

    if not issues:
        print("✓ All g0 nodes have observability and grounding.")
        return 0

    print("⚠ G0 nodes with gaps:\n")
    for issue in issues:
        print(f"  {issue['id']}")
        print(f"    One-liner: {issue['one_liner']}")
        print(f"    Missing: {', '.join(issue['missing'])}")
        print()

    print(f"\nSummary: {len(issues)}/{len(g0_nodes)} g0 nodes have gaps.")
    print("\nNote: This is advisory. Review against g0-gene-checklist.md before proposing to the form.")

    return 1 if issues else 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 bin/validate-g0-genes.py <yaml_path>")
        sys.exit(1)

    sys.exit(validate_g0_genes(sys.argv[1]))
