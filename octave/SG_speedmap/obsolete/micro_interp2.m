%function ZI = micro_interp2(x1,y1,z1,x2,y2,z2,XI,YI,method)
% Dang Doan. 2016.12.07
% Interpolate the value ZI for the point (XI,YI) which is between the 4 points:
%              (x2,y2)
%
% (x3,y3)      (XI,YI)       (x4,y4)
%
%              (x1,y1)
% with:
% f(x1,y1)=z1
% f(x2,y2)=z2
% f(x3,y3)=z3
% f(x3,y4)=z4
% Compute: ZI=f(XI,YI)
% Note: we do NOT need y1=y2, x1!=x2, x3=x4, y3!=y4 

function ZI = micro_interp2(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,XI,YI,method)
  %narginchk (1, 7);
  %nargs = nargin;
  if nargin < 15 
    method = "linear";
  end
  
    if (strcmp (method, "linear"))
      ## use (linear) weighted average
      d1=pair_distance(x1,y1,XI,YI);
      d2=pair_distance(x2,y2,XI,YI);
      d3=pair_distance(x3,y3,XI,YI);
      d4=pair_distance(x4,y4,XI,YI);
      
      % to do: check the condition d1+d2+d3+d4!=0
      ZI = (z1*d1 + z2*d2 + z3*d3 + z4*d4)/(d1+d2+d3+d4);
    end  
%    elseif (strcmp (method, "nearest"))
%      ii = (XI - X(xidx) >= X(xidx + 1) - XI);
%      jj = (YI - Y(yidx) >= Y(yidx + 1) - YI);
%      idx = sub2ind (size (Z), yidx+jj, xidx+ii);
%      ZI = Z(idx);
%
%    elseif (strcmp (method, "pchip") || strcmp (method, "cubic"))
%
%      if (length (X) < 2 || length (Y) < 2)
%        error ("interp2: %s requires at least 2 points in each dimension",
%               method);
%      endif
%
%      ## first order derivatives
%      DX = __pchip_deriv__ (X, Z, 2);
%      DY = __pchip_deriv__ (Y, Z, 1);
%      ## Compute mixed derivatives row-wise and column-wise, use the average.
%      DXY = (__pchip_deriv__ (X, DY, 2) + __pchip_deriv__ (Y, DX, 1))/2;
%
%      ## do the bicubic interpolation
%      hx = diff (X); hx = hx(xidx);
%      hy = diff (Y); hy = hy(yidx);
%
%      tx = (XI - X(xidx)) ./ hx;
%      ty = (YI - Y(yidx)) ./ hy;
%
%      ## construct the cubic hermite base functions in x, y
%
%      ## formulas:
%      ## b{1,1} =    ( 2*t.^3 - 3*t.^2     + 1);
%      ## b{2,1} = h.*(   t.^3 - 2*t.^2 + t    );
%      ## b{1,2} =    (-2*t.^3 + 3*t.^2        );
%      ## b{2,2} = h.*(   t.^3 -   t.^2        );
%
%      ## optimized equivalents of the above:
%      t1 = tx.^2;
%      t2 = tx.*t1 - t1;
%      xb{2,2} = hx.*t2;
%      t1 = t2 - t1;
%      xb{2,1} = hx.*(t1 + tx);
%      t2 += t1;
%      xb{1,2} = -t2;
%      xb{1,1} = t2 + 1;
%
%      t1 = ty.^2;
%      t2 = ty.*t1 - t1;
%      yb{2,2} = hy.*t2;
%      t1 = t2 - t1;
%      yb{2,1} = hy.*(t1 + ty);
%      t2 += t1;
%      yb{1,2} = -t2;
%      yb{1,1} = t2 + 1;
%
%      ZI = zeros (size (XI));
%      for i = 1:2
%        for j = 1:2
%          zidx = sub2ind (size (Z), yidx+(j-1), xidx+(i-1));
%          ZI += xb{1,i} .* yb{1,j} .*   Z(zidx);
%          ZI += xb{2,i} .* yb{1,j} .*  DX(zidx);
%          ZI += xb{1,i} .* yb{2,j} .*  DY(zidx);
%          ZI += xb{2,i} .* yb{2,j} .* DXY(zidx);
%        endfor
%      endfor
%
%    endif
end