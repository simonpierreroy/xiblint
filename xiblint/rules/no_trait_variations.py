"""
Checks for Trait Variations being enabled.
"""

from xiblint.rules import Rule


class NoTraitVariations(Rule):
    def check(self, context):  # type: (Rule, xiblint.xibcontext.XibContext) -> None
        root = context.tree.getroot()
        if root.get('useTraitCollections') == 'YES' and root.get('targetRuntime') != 'watchKit':
            context.error(root, "Document has 'Use Trait Variations' enabled")
