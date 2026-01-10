import re
import random
from core.config import MAX_DICE, MAX_FACES

TERM_PATTERN = re.compile(r"[+-]?\s*[^+-]+")

DICE_TERM_PATTERN = re.compile(
    r"""
    (\d+)              # quantidade
    d
    (\d+)              # faces
    \s*
    (k[hl](\d+)?)?     # kh / kl / kh2 / kl3
    """,
    re.VERBOSE | re.IGNORECASE
)

class RollResult:
    def __init__(self, total: int, detalhes: list[str], error: str | None = None):
        self.total = total
        self.detalhes = detalhes
        self.error = error

    def is_error(self) -> bool:
        return self.error is not None


def roll_expression(expr: str) -> RollResult:
    terms = TERM_PATTERN.findall(expr)
    if not terms:
        return RollResult(0, [], None)

    total = 0
    detalhes = []

    for term in terms:
        term = term.strip()
        sign = -1 if term.startswith("-") else 1
        clean = term.lstrip("+-").strip()

        match = DICE_TERM_PATTERN.fullmatch(clean)

        if match:
            qtd, faces, keep_raw, keep_n = match.groups()
            qtd = int(qtd)
            faces = int(faces)

            if qtd > MAX_DICE:
                return RollResult(0, [], f"Máximo de dados permitido: {MAX_DICE}")

            if faces > MAX_FACES:
                return RollResult(0, [], f"Máximo de faces permitido: {MAX_FACES}")

            resultados = [random.randint(1, faces) for _ in range(qtd)]
            usados = resultados.copy()

            # 🔝 KEEP
            if keep_raw:
                keep_type = keep_raw[:2]
                keep_count = int(keep_n) if keep_n else 1

                if keep_count > qtd:
                    return RollResult(0, [], "Não é possível manter mais dados do que foram rolados.")

                resultados_ordenados = sorted(
                    resultados,
                    reverse=(keep_type == "kh")
                )
                usados = resultados_ordenados[:keep_count]

            subtotal = sum(usados) * sign
            total += subtotal

            detalhes.append(
                f"{term} → {resultados} → {subtotal}"
            )

        else:
            try:
                valor = int(clean) * sign
                total += valor
                detalhes.append(f"{term} → {valor}")
            except ValueError:
                # Ignorar termos inválidos em vez de retornar erro
                continue

    return RollResult(total, detalhes)
