"""
tasks is the namespace manager for invoke tasks.
"""

from invoke import Collection

from tasks import style


namespace = Collection()
namespace.add_collection(style)
