import argparse
import logging
import random
from dataclasses import dataclass, field
from typing import List

#!/usr/bin/env python3
"""Dummy boilerplate for Assign_Roles-Bot."""

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

@dataclass
class User:
    id: int
    name: str
    roles: List[str] = field(default_factory=list)

    def add_role(self, ro: str) -> None:
        if ro not in self.roles:
            self.roles.append(ro)
            logger.debug("Added role %s to %s", ro, self.name)

    def remove_role(self, role: str) -> None:
        if role in self.roles:
            self.roles.remove(role)
            logger.debug("Removed role %s from %s", role, self.name)

def generate_dummy_users(n: int) -> List[User]:
    return [User(id=i, name=f"user{i}") for i in range(1, n+1)]

def assign_random_roles(users: List[User], roles: List[str]) -> None:
    for u in users:
        chosen = random.sample(roles, k=random.randint(0, min(len(roles), 3)))
        for r in chosen:
            u.add_role(r)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Dummy role assigner")
    p.add_argument("--count", "-c", type=int, default=5, help="Number of users")
    p.add_argument("--seed", type=int, default=None, help="Random seed")
    return p.parse_args()

def main() -> int:
    args = parse_args()
    if args.seed is not None:
        random.seed(args.seed)
    users = generate_dummy_users(args.count)
    roles = ["admin", "moderator", "member", "guest"]
    assign_random_roles(users, roles)
    for u in users:
        logger.info("%s (%d): %s", u.name, u.id, ", ".join(u.roles) or "no roles")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())