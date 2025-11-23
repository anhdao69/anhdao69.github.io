puts "[liquid_taint_patch] Loaded Liquid taint patch"

module Liquid
  class Variable
    private

    # Jekyll/Liquid calls this internally before rendering variables.
    # On old Ruby it checked obj.tainted?, but on Ruby 3.2+ taint is gone.
    # We just no-op it.
    def taint_check(_obj)
      # do nothing
    end
  end
end
